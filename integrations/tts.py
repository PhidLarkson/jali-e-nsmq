import requests
from pydub import AudioSegment
from pydub.playback import play
import io

def text_to_speech(text):
    api_url = "https://f6aa-34-19-43-141.ngrok-free.app/synthesize_audios1"
    params = {
        "text": text
    }
    response = requests.get(api_url, json=params)
    
    if response.status_code == 200:
        audio_data = response.content
        audio = AudioSegment.from_file(io.BytesIO(audio_data), format="wav")
        play(audio)
    else:
        print("Error:", response.status_code)
        print("Failed to play audio")