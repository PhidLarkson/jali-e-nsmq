import requests
import json

def translation(text, target_language):
    url = "https://translation-api.ghananlp.org/v1/translate"
    headers = {
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache',
        'Ocp-Apim-Subscription-Key': '', # put your API key here
    }
    data = {
        'in': text,
        'lang': target_language
    }
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
         return response.json()
    else:
         return "An error occured"

# language_choice = "en-tw"
# translated_text = translate("Hello, how are you?", "en-tw")
# print(translated_text)
def convert_text_to_speech(text):
    try:
        url = "https://translation-api.ghananlp.org/tts/v1/tts"

        hdr = {
            # Request headers
            'Content-Type': 'application/json',
            'Cache-Control': 'no-cache',
            'Ocp-Apim-Subscription-Key': '', # put your API key here
        }
        # Request body
        data = json.dumps({"text": text, "language": "tw"})
        req = requests.post(url, headers=hdr, data=bytes(data.encode("utf-8")))
        req.get_method = lambda: 'POST'
        response = req
        return response
    except Exception as e:
        return "Failed to save audio file"
    


        

            # print("Failed to save audio file")