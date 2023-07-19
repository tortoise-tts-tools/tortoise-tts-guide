

trimmed_lines = [line.strip() for line in text.split('\n') if line.strip()]


voice = 'train_dotrice' # select voice

audio_list = []
voice_samples, conditioning_latents = load_voice(voice)
!mkdir out
i = 0
for txt in trimmed_lines:
    i+= 1
    #@markdown Load it and send it through Tortoise.
    gen = tts.tts_with_preset(txt, voice_samples=voice_samples, conditioning_latents=conditioning_latents, preset=preset, k=1)
    torchaudio.save(f'out/generated_{i}.wav', gen.squeeze(0).cpu(), 24000)
    del gen
    gc.collect()
