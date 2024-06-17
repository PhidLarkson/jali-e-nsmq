from faster_whisper import WhisperModel
from pydub import AudioSegment
from pydub.playback import play
import sounddevice as sd
from scipy.io.wavfile import write

model_size = "distil-large-v3"
fs = 44100  # Sample rate
seconds = 20  # Duration of recording

output = ""

def main(fs, seconds):
    # Record audio
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2, dtype='int16')
    # beep to indicate the start of recording
    play(AudioSegment.from_file("integrations/blip-131856.mp3"))

    print("Recording Audio")
    sd.wait()  # Wait until recording is finished
    print("Audio recording complete , Play Audio")

    #beep again to indicate the end of recording
    play(AudioSegment.from_file("integrations/blip-131856.mp3"))

    # Save as WAV file
    write('temp.wav', fs, myrecording)  # Save as WAV file

    # URL of the file to transcribe

    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    # segmwnts
    segments, info = model.transcribe("temp.wav", beam_size=5, language="en", condition_on_previous_text=False)

    for segment in segments:
        # print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
        output += segment.text

    print(output)

    return output