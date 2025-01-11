import pyaudio
import wave
import requests

def record_audio(filename, record_seconds=5):
    chunk = 1024
    format = pyaudio.paInt16
    channels = 1
    rate = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    print("Recording...")
    frames = []

    for _ in range(0, int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

def send_to_processor(filename, processor_url):
    with open(filename, 'rb') as f:
        files = {'file': f}
        response = requests.post(processor_url, files=files)
        return response.text

def record_and_send(processor_url, record_seconds=5):
    filename = "recorded_audio.wav"
    record_audio(filename, record_seconds)
    response = send_to_processor(filename, processor_url)
    return response

class TestAudioRecording(unittest.TestCase):
    def setUp(self):
        self.filename = "test_recorded_audio.wav"
        self.processor_url = "http://example.com/processor"
        self.record_seconds = 5

    def test_record_audio(self):
        record_audio(self.filename, self.record_seconds)
        self.assertTrue(os.path.exists(self.filename))
        os.remove(self.filename)

    @patch('requests.post')
    def test_send_to_processor(self, mock_post):
        mock_response = MagicMock()
        mock_response.text = "Success"
        mock_post.return_value = mock_response

        with open(self.filename, 'wb') as f:
            f.write(b'dummy audio data')

        response = send_to_processor(self.filename, self.processor_url)
        self.assertEqual(response, "Success")
        os.remove(self.filename)

    @patch('requests.post')
    def test_record_and_send(self, mock_post):
        mock_response = MagicMock()
        mock_response.text = "Success"
        mock_post.return_value = mock_response

        response = record_and_send(self.processor_url, self.record_seconds)
        self.assertEqual(response, "Success")
        self.assertTrue(os.path.exists("recorded_audio.wav"))
        os.remove("recorded_audio.wav")

if __name__ == '__main__':
    import unittest
    import os
    from unittest.mock import patch, MagicMock
    unittest.main()
