ffmpeg -f concat -i <(for f in *.wav; do echo "file '$PWD/$f'"; echo "duration 0.25"; done) -c copy output.wav
