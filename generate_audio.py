import torch
import torchaudio
import torch.nn as nn
import torch.nn.functional as F
import IPython
from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_audio, load_voice, load_voices
import nltk
nltk.download('punkt')
tts = TextToSpeech(use_deepspeed=True, kv_cache=True, half=True)
text = "Joining two modalities results in a surprising increase in generalization! What would happen if we combined them all?"
preset = "ultra_fast"
voice = 'train_dotrice'
script = text.replace("\n", " ").strip()
sentences = nltk.sent_tokenize(script)
audio_list = []
for txt in sentences:
    voice_samples, conditioning_latents = load_voice(voice)
    gen = tts.tts_with_preset(txt, voice_samples=voice_samples, conditioning_latents=conditioning_latents, preset=preset)
    audio_list.append(gen.squeeze(0).cpu())
concatenated_audio = torch.cat(audio_list, dim=1)
torchaudio.save('generated.wav', concatenated_audio, 24000)
