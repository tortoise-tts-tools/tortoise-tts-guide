<img src="banner.png" width=300>

# tortoise-tts-guide

Jump to: [Inference](#inference) - [Fine-Tuning](#fine-tuning)

Tortoise (TorToiSe) TTS is one of the best TTS (text-to-speech) programs available. In fact, it is even rumored to power the popular ElevenLabs TTS service.

The goal of this is to make Tortoise TTS accessible for all, without having to pay for ElevenLabs!

Tortoise TTS is remarkably slow, however there are several enhancements we can use to speed it up.

Before we begin: I do NOT endorse any repo/website/etc linked here. USE AT YOUR OWN RISK!!!

## Discuss (all things) Tortoise TTS

[Discussions](https://github.com/fakerybakery/tortoise-tts-guide/discussions)

## About

This is a multi-part work-in-progress series about running + finetuning tortoise TTS. If you're serious about finetuning it, please consider using a paid Colab GPU or a hosting provider.

## The Goal

Eventually, the goal is to create audiobooks from public domain books and release them for free or for a minimal charge. Unfortunately, further fine-tuning must be done to create models with quality that allows this.

## Demo

"The Raven" by Edgar Allan Poe. Generated using voice `train_dotrice`.

<a href="https://github.com/fakerybakery/tortoise-tts-guide/raw/main/raven.mp3" download>Download File</a>

I generated this on a free Colab instance (T4 GPU).

## Speed

On all the fastest settings, the speed has an approximate 1:2 ratio (1 minute of audio takes 2 minutes to generate) on a free Colab instance. It will likely be many times faster on better GPUs, such as A100/A10Gs.

## Introduction

Tortoise TTS recently gained a new maintainer, @manmay-nakhashi. Before becoming the Tortoise maintainer, he created [`tortoise-tts-fastest`](https://github.com/manmay-nakhashi/tortoise-tts-fastest), a fork of [`tortoise-tts-fast`](https://github.com/152334H/tortoise-tts-fast). The author of `tortoise-tts-fast`, @152334H, [works for ElevenLabs](https://github.com/152334H) and created a forked version of [`DL-Art-School`](https://github.com/152334H/DL-Art-School). `DL-Art-School` was originally created by the author of Tortoise TTS, however he did not release finetuning code due to ["ethical"](https://github.com/neonbjb/tortoise-tts/discussions/292#discussioncomment-4876055) and legal concerns. The forked version supports finetuning Tortoise TTS, which we will use in the fine-tuning section. Fine-tuning requires a certain DVAE model, which the author meant to keep from the public, but he accidentally pushed the model to HuggingFace (and later deleted it). Oops! Thankfully, various people have saved archives of the model, **and it's still available in the Hugging Face commit history.** You can download the model [here](https://huggingface.co/jbetker/tortoise-tts-v2/resolve/3704aea61678e7e468a06d8eea121dba368a798e/.models/dvae.pth) (open an Issue if the link goes down), but you won't need it because it will automatically be downloaded when needed. But feel free to archive a copy.

## Notes

 - If any of these repositories becomes unavailable, please open an Issue (I've tried to archived most of them)
 - On Colab, inference + training will be extremely slow. Please consider using a cloud provider (they're really not that expensive, and you can get hundreds of dollars in free credits)

## Before you start

If you don't have a CUDA GPU, this may not work.

## Easy GUI for Inference + Training Interface

This is the easiest way to train + use the interface.

<a target="_blank" href="https://colab.research.google.com/github/fakerybakery/tortoise-tts-guide/blob/main/mrq_colab.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

## Inference

Basically, if you want a simple GUI, use the section above.

**COMING SOON:** How to load a custom model

To start Inference, we will use the main `tortoise-tts` repo. Another possibility is to use [this solution](https://git.ecker.tech/mrq/ai-voice-cloning/) (which I have tested for inference)

Click the button below:

<a target="_blank" href="https://colab.research.google.com/github/fakerybakery/tortoise-tts-guide/blob/main/tortoise_tts.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

[Download](https://raw.githubusercontent.com/fakerybakery/tortoise-tts-guide/main/tortoise_tts.ipynb)

**UPDATE: We no longer need to use `tortoise-tts-fastest` as it seems to be abandoned as the changes have been merged upstream. If you still want to use it, click [here](https://colab.research.google.com/github/fakerybakery/tortoise-tts-guide/blob/main/tortoise_tts_fast.ipynb) ([download](https://raw.githubusercontent.com/fakerybakery/tortoise-tts-guide/main/tortoise_tts_fast.ipynb))**

(The notebook now works after much tweaking.)

On a free colab, generating the first stanza of The Raven by Edgar Allan Poe (9 seconds) took around 24 seconds. Not the fastest, but much better than before.

Fill out all the forms (`text` is the text you want it to say)

Select a GPU (in the menu, go to `Runtime` > `Change runtime type` > `Hardware accelerator`. Select `GPU`. Click `Save`.

Press the run/play button next to each cell. Listen to the audio.

```python
text = """
your
multiline
audiobook
"""
trimmed_lines = [line.strip() for line in text.strip().split('\n') if line.strip()]
```

Then, make another Code cell:

```python
audio_list = []
voice = 'train_dotrice' #@param {type:"string"}
for txt in trimmed_lines:

    #@markdown Load it and send it through Tortoise.
    voice_samples, conditioning_latents = load_voice(voice)
    gen = tts.tts_with_preset(txt, voice_samples=voice_samples, conditioning_latents=conditioning_latents, 
                              preset=preset)
    audio_list.append(gen.squeeze(0).cpu())
concatenated_audio = torch.cat(audio_list, dim=1)
torchaudio.save('generated.wav', concatenated_audio, 24000)
IPython.display.Audio('generated.wav')
```


## Fine-Tuning

Basically, if you want a simple GUI, use the section above.

Custom-tuning coming soon...

## Resources

- [Tortoise TTS + WebUI (AKA "the mrq repo")](https://git.ecker.tech/mrq/ai-voice-cloning)
- [Tortoise TTS](https://github.com/neonbjb/tortoise-tts)
- [Tortoise TTS Fast](https://github.com/152334H/tortoise-tts-fast)
- [Tortoise TTS Fastest](https://github.com/manmay-nakhashi/tortoise-tts-fastest)
- [DL Art School](https://github.com/neonbjb/DL-Art-School)
- [DL Art School Fork for Tortoise TTS](https://github.com/152334H/DL-Art-School)
- [Tortoise TTS on Hugging Face](https://huggingface.co/jbetker/tortoise-tts-v2)
- [Tortoise TTS DVAE Download](https://huggingface.co/jbetker/tortoise-tts-v2/resolve/3704aea61678e7e468a06d8eea121dba368a798e/.models/dvae.pth)

## License

This document and all modifications to the notebooks are licensed under CC-BY-NC-SA 4.0. If you want to use these materials for commercial purposes (e.g. making an audiobook/podcast/etc), please open an Issue. For attribution, please add attribution in the audio itself.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
