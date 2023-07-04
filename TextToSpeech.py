import requests

def create_audio(text: str, language: str):
        url = "https://play.ht/api/v1/convert"

        payload = {
            "content": [text],
            "voice": language
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "AUTHORIZATION": "Bearer 2873a53468cb4dd08f05af73952f1eb5",
            "X-USER-ID": "LKuNwQ5149TDU3rVBrz3on73Fbw2"
        }
        response = requests.post(url, json=payload, headers=headers)
        return str(response.json()["transcriptionId"])
    
def find_audio(transcriptionId: str):
        url = "https://play.ht/api/v1/articleStatus?transcriptionId=" + transcriptionId
        headers = {
            "accept": "application/json",
            "AUTHORIZATION": "Bearer 2873a53468cb4dd08f05af73952f1eb5",
            "X-USER-ID": "LKuNwQ5149TDU3rVBrz3on73Fbw2"
        }

        response = requests.get(url, headers=headers)
        return str(response.json()["audioUrl"])