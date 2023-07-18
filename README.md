# tortoise-tts-guide

Jump to: [Inference](#inference) - [Fine-Tuning](#fine-tuning)

Tortoise TTS stands as a leading text-to-speech (TTS) program renowned for its exceptional capabilities. It has gained considerable recognition, with some suggesting that it may power the highly acclaimed ElevenLabs TTS service.

My primary objective is to ensure the accessibility of Tortoise TTS to a wider audience, eliminating the need for costly ElevenLabs subscriptions. Although Tortoise TTS exhibits a noticeably slower performance, there exist numerous enhancements at our disposal to optimize its speed and efficiency.

It is important to note that I do not endorse any models listed in this guide. Use this guide at your own risk!

## Discuss (all things) Tortoise TTS

[Discussions](https://github.com/fakerybakery/tortoise-tts-guide/discussions)

## About

This is a multi-part work-in-progress series about running + finetuning tortoise TTS. If you're serious about finetuning it, please consider using a paid Colab GPU or a cloud hosting provider.

## The Goal

Ultimately, our objective is to produce audiobooks derived from public domain books and distribute them either for free or at a minimal cost. However, achieving this goal requires additional refinement in order to develop high-quality models that meet the necessary standards.

By dedicating time to further fine-tuning, we can ensure that the resulting models possess the desired level of quality and fidelity required for the creation of these audiobooks. This meticulous process will enable us to provide accessible and enjoyable content to a wide audience while maintaining the integrity of the original literary works.

## Demo

"The Raven" by Edgar Allan Poe. Generated using voice `train_dotrice`.

<a href="https://github.com/fakerybakery/tortoise-tts-guide/raw/main/raven.mp3" download>Download File</a>

I generated this on a free Colab instance (T4 GPU).

## Speed

When employing the fastest settings on a free Colab instance, the synthesis speed exhibits an approximate ratio of 1:2, indicating that generating 1 minute of audio takes approximately 2 minutes. However, it is crucial to note that utilizing superior GPUs like A100 or A10Gs is expected to yield significantly faster results, potentially achieving a substantially higher synthesis speed compared to the aforementioned ratio.

## Introduction

Tortoise TTS has recently welcomed a new maintainer, @manmay-nakhashi, who has made notable contributions to the project. Prior to taking on this role, @manmay-nakhashi developed the forked version called [`tortoise-tts-fastest`](https://github.com/manmay-nakhashi/tortoise-tts-fastest), derived from the original repository [`tortoise-tts-fast`](https://github.com/152334H/tortoise-tts-fast), which was created by @152334H, an employee at ElevenLabs, as evident from their GitHub profile.

It is worth mentioning that @152334H also created a modified version of [`DL-Art-School`](https://github.com/152334H/DL-Art-School), another project associated with the author of Tortoise TTS. While the original author refrained from releasing the finetuning code for ethical and legal considerations, @152334H's forked version supports the finetuning process, which will be utilized in the upcoming fine-tuning section.

The fine-tuning procedure requires a specific DVAE model, initially intended to be kept private by the author. However, an accidental push to Hugging Face made the model briefly accessible before being deleted. Fortunately, several individuals have archived copies of the model, and it is still available in the commit history of the Hugging Face repository. You can download the model [here](https://huggingface.co/jbetker/tortoise-tts-v2/resolve/3704aea61678e7e468a06d8eea121dba368a798e/.models/dvae.pth) (please open an Issue if the link becomes unavailable). Although the model will be automatically downloaded when required, you are welcome to create an additional archive copy for safekeeping.

## Notes

- In the event that any of these repositories become inaccessible, kindly open an Issue to notify the relevant parties. Efforts have been made to archive most of the repositories to ensure their availability.
- It is important to note that running inference and conducting training on Colab may result in exceedingly slow processes. To mitigate this, I strongly recommend considering the utilization of a cloud provider. Cloud providers offer efficient computing resources at reasonable costs, and you may even be eligible for substantial free credits, allowing you to experiment without incurring significant expenses.

## Before you start

Please note that having a CUDA GPU is essential for the successful execution of this process. If you do not possess a CUDA-compatible GPU, there is a possibility that the following steps may not function as intended.

## GUI

Experience the convenience of utilizing a user-friendly graphical interface for both inference and training purposes with ease.

<a target="_blank" href="https://colab.research.google.com/github/fakerybakery/tortoise-tts-guide/blob/main/mrq_colab.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

## Inference

For a simplified GUI experience, refer to the section above.

**COMING SOON:** Guide on loading a custom model.

To initiate the inference process, we will utilize the primary `tortoise-tts` repository. Alternatively, you can explore [this solution](https://git.ecker.tech/mrq/ai-voice-cloning/) (which I have personally tested for inference).

Click the button below to begin:

<a target="_blank" href="https://colab.research.google.com/github/fakerybakery/tortoise-tts-guide/blob/main/tortoise_tts.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

[Download](https://raw.githubusercontent.com/fakerybakery/tortoise-tts-guide/main/tortoise_tts.ipynb)

**UPDATE: The use of `tortoise-tts-fastest` is no longer necessary as it appears to have been abandoned, with the changes merged upstream. However, if you still wish to use it, click [here](https://colab.research.google.com/github/fakerybakery/tortoise-tts-guide/blob/main/tortoise_tts_fast.ipynb) ([download](https://raw.githubusercontent.com/fakerybakery/tortoise-tts-guide/main/tortoise_tts_fast.ipynb)).**

## Fine-Tuning

For a simplified GUI experience, refer to the section above.

Guide for custom fine-tuning is coming soon...

## Resources

- [Tortoise TTS + WebUI (also known as "the mrq repo")](https://git.ecker.tech/mrq/ai-voice-cloning)
- [Tortoise TTS](https://github.com/neonbjb/tortoise-tts)
- [Tortoise TTS Fast](https://github.com/152334H/tortoise-tts-fast)
- [Tortoise TTS Fastest](https://github.com/manmay-nakhashi/tortoise-tts-fastest)
- [DL Art School](https://github.com/neonbjb/DL-Art-School)
- [DL Art School Fork for Tortoise TTS](https://github.com/152334H/DL-Art-School)
- [Tortoise TTS on Hugging Face](https://huggingface.co/jbetker/tortoise-tts-v2)
- [Download Tortoise TTS DVAE Model](https://huggingface.co/jbetker/tortoise-tts-v2/resolve/3704aea61678e7e468a06d8eea121dba368a798e/.models/dvae.pth)

## Tortoise Tips

Custom model path (for finetuned model):

```python
from tortoise.api import TextToSpeech
tts = TextToSpeech(use_deepspeed=True, kv_cache=True, half=True, models_dir="<Model Directory>")
```

## License

Different parts of this repository are governed by various licenses. Please refer to the [license statement](LICENSE.md) for further details.
