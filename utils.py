from io import BytesIO
import io
import librosa
import soundfile

def apply_time_stretching(audio_data,playback_speed):
    y, sr = librosa.load(BytesIO(audio_data), sr=None)  # sr is sampling rate

    # Perform time stretching using librosa
    stretched_y = librosa.effects.time_stretch(y, rate=playback_speed)

    stretched_audio = io.BytesIO()

    # Use the updated `soundfile.write` for audio output (compatible)
    soundfile.write(stretched_audio, stretched_y, sr)

    # Rewind the in-memory file for reading
    stretched_audio.seek(0)

    # Return the stretched audio data as bytes
    return stretched_audio.read()