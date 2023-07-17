# tortoise-tts-guide

Tortoise (TorToiSe) TTS is one of the best TTS (text-to-speech) programs available. In fact, it is even rumored to power the popular ElevenLabs TTS service.

Tortoise TTS is remarkably slow, however there are several enhancements we can use to speed it up.

Before we begin: I do NOT endorse any repo/website/etc linked here. USE AT YOUR OWN RISK!!!

Tortoise TTS recently gained a new maintainer, @manmay-nakhashi. Before becoming the Tortoise maintainer, he created [`tortoise-tts-fastest`](https://github.com/manmay-nakhashi/tortoise-tts-fastest), a fork of [`tortoise-tts-fast`](https://github.com/152334H/tortoise-tts-fast). The author of `tortoise-tts-fast`, @152334H, [works for ElevenLabs](https://github.com/152334H) and created a forked version of [`DL-Art-School`](https://github.com/152334H/DL-Art-School). `DL-Art-School` was originally created by the author of Tortoise TTS, however he did not release finetuning code due to ["ethical"](https://github.com/neonbjb/tortoise-tts/discussions/292#discussioncomment-4876055) and legal concerns. The forked version supports finetuning Tortoise TTS, which we will use in the fine-tuning section. Fine-tuning requires a certain DVAE model, which the author meant to keep from the public, but he accidentally pushed the model to HuggingFace (and later deleted it). Oops! Thankfully, various people have saved archives of the model, **and it's still available in the Hugging Face commit history.** You can download the model [here] (open an Issue if the link goes down), but you won't need it because it will automatically be downloaded when needed. But feel free to archive a copy.

## Note

If any of these repositories becomes unavailable, please open an Issue (I've tried to archived most of them)

## Inference

To start Inference, we will use `tortoise-tts-fastest`. Another possibility is to use [this solution](https://git.ecker.tech/mrq/ai-voice-cloning/) (which I have tested for inference)

. . .

[To Be Continued...]
