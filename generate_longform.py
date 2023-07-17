
audio_list = []

# Loop through each text in the array
voice = 'train_dotrice' #@param {type:"string"}
for txt in text:

    #@markdown Load it and send it through Tortoise.
    voice_samples, conditioning_latents = load_voice(voice)
    gen = tts.tts_with_preset(txt, voice_samples=voice_samples, conditioning_latents=conditioning_latents, 
                              preset=preset)
    
    # Append generated audio tensor to the list
    audio_list.append(gen.squeeze(0).cpu())

# Concatenate audio tensors in the list
concatenated_audio = torch.cat(audio_list, dim=1)

# Save the concatenated audio
torchaudio.save('generated.wav', concatenated_audio, 24000)

# Display the concatenated audio
ipd.Audio('generated.wav')
