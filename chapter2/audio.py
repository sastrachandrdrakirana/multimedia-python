from pydub import AudioSegment
import simpleaudio as sa
# Memuat file audio
audio = AudioSegment.from_file('ghiblisound.mp3')
audio = AudioSegment.from_file('ghiblisound.mp3')
audio.export('result.mp3', format='mp3')
clipped_audio = audio[:10000]
clipped_audio.export('clipped_result.mp3', format='mp3')
combined_audio = audio + clipped_audio
combined_audio.export('combined_result.mp3', format='mp3')
audio.export('result.wav', format='wav')
# Memutar audio
wave_obj = sa.WaveObject.from_wave_file('result.wav')
play_obj = wave_obj.play()

# Menunggu sampai audio selesai diputar
play_obj.wait_done()
louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
louder_audio.export('louder_result.mp3', format='mp3')
