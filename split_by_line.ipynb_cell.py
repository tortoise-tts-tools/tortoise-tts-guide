trimmed_lines = [line.strip() for line in text.split('\n') if line.strip()]


voice = 'train_dotrice' # select voice

audio_list = []
voice_samples, conditioning_latents = load_voice(voice)
for txt in trimmed_lines:

    #@markdown Load it and send it through Tortoise.
    gen = tts.tts_with_preset(txt, voice_samples=voice_samples, conditioning_latents=conditioning_latents, preset=preset, k=1)
    audio_list.append(gen.squeeze(0).cpu())
concatenated_audio = torch.cat(audio_list, dim=1)
torchaudio.save('generated.wav', concatenated_audio, 24000)
IPython.display.Audio('generated.wav')
