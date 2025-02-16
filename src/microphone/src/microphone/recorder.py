import pyaudio
import math
import struct
import wave
import time
import os

Threshold = 10

SHORT_NORMALIZE = 1.0 / 32768.0
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
swidth = 2


class ConversationRecorder:

    @staticmethod
    def rms(frame) -> float:
        """Calculate the RMS of a frame"""
        count = len(frame) / swidth
        format = "%dh" % (count)
        shorts = struct.unpack(format, frame)

        sum_squares = 0.0
        for sample in shorts:
            n = sample * SHORT_NORMALIZE
            sum_squares += n * n
        rms = math.pow(sum_squares / count, 0.5)

        return rms * 1000

    def __init__(
        self,
        threshold: float = 0.03,  # Volume threshold to detect speech
        silence_limit: float = 7.0,  # Seconds of silence to mark end of conversation
        prev_audio_seconds: float = 0.5,  # Seconds of audio to prepend before detection
        format: int = pyaudio.paInt16,  # Format of the audio
        channels: int = 1,  # Number of channels
        rate: int = 16000,  # Sample rate
        chunk: int = 1024,  # Chunk size
        output_dir: str = f"{os.getcwd()}/recordings",  # Output directory
    ) -> None:
        self.threshold = threshold
        self.silence_limit = silence_limit
        self.prev_audio_seconds = prev_audio_seconds
        self.format = format
        self.channels = channels
        self.rate = rate
        self.chunk = chunk
        self.output_dir = output_dir

        # Create output directory if it doesn't exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        # Initialize PyAudio
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            output=True,
            frames_per_buffer=self.chunk,
        )

    def record(self):
        """Record a conversation"""
        print("Noise detected, recording beginning")
        rec = []
        current = time.time()
        end = time.time() + self.silence_limit

        while current <= end:
            data = self.stream.read(chunk)
            if self.rms(data) >= Threshold:
                end = time.time() + self.silence_limit
            current = time.time()
            rec.append(data)
        self.write(b"".join(rec))

    def write(self, recording):
        """Write the recording to a file"""
        n_files = len(os.listdir(self.output_dir))

        filename = os.path.join(self.output_dir, "{}.wav".format(n_files))

        wf = wave.open(filename, "wb")
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(recording)
        wf.close()
        print("Written to file: {}".format(filename))
        print("Returning to listening")

    def listen(self) -> None:
        """Monitor the microphone for conversations"""
        print("Listening for conversations...")
        try:
            while True:
                input = self.stream.read(self.chunk)
                rms_val = self.rms(input)
                if rms_val > self.threshold:
                    self.record()
        except KeyboardInterrupt:
            print("Monitoring stopped by user")
        finally:
            self.stream.stop_stream()
            self.stream.close()
            self.p.terminate()
