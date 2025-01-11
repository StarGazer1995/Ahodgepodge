import whisper
import sounddevice as sd
import numpy as np
import wave
import os 

WHISP_PATH=os.path.join(os.dirname(__file__), "whisper/whisper-large-v3")
def record_audio(duration=5, samplerate=16000):
    print("Recording...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float32')
    sd.wait()
    print("Recording finished.")
    return audio.flatten()

def save_audio_to_wav(audio, filename="output.wav", samplerate=16000):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(np.int16(audio * 32767).tobytes())

def transcribe_audio(filename="output.wav"):
    result= whisper.transcribe(filename, path_or_hf_repo=WHISP_PATH)["text"]
    return result["text"]

def record_and_transcribe(duration=5):
    audio = record_audio(duration)
    save_audio_to_wav(audio)
    return transcribe_audio()

# Unit test
import unittest
import os

class TestTranscription(unittest.TestCase):
    def test_transcription(self):
        # Create a dummy audio file with a known phrase
        dummy_audio = np.zeros(16000 * 5)  # 5 seconds of silence
        save_audio_to_wav(dummy_audio, "test.wav")
        
        # Transcribe the dummy audio
        transcription = transcribe_audio("test.wav")
        
        # Check if the transcription is a string (even if empty)
        self.assertIsInstance(transcription, str)
        
        # Clean up
        os.remove("test.wav")

if __name__ == "__main__":
    unittest.main()
