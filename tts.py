import websocket
import json
import ssl
import os
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY_NAME")
authenticator = IAMAuthenticator(api_key)

access_token = authenticator.token_manager.get_token()

ws_url = "wss://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/c6e2342d-5802-4efc-96d1-682b5fa6fe75"

voice = "en-US_KevinV3Voice"
rate = 1.2

wsURI = f"{ws_url}/v1/synthesize?access_token={access_token}&voice={voice}&rate_percentage={rate}"


def text_to_speech(text: str, out_path: str) -> tuple:
    ws = websocket.create_connection(wsURI, sslopt={"cert_reqs": ssl.CERT_NONE})

    message = {
        'text': text,
        'accept': 'audio/mp3',
        'timings': ['words']
    }

    ws.send(json.dumps(message))
    ws.recv()

    words = []
    timings = []
    with open(out_path, 'wb') as output_audio:
        while True:
            stream = ws.recv()

            if len(stream) == 0:
                break

            if type(stream) == str:
                word_timings = json.loads(stream)
                words.append(word_timings['words'][0][0])
                timings.append(word_timings['words'][0][1:])

            elif type(stream) == bytes:
                output_audio.write(stream)

    return words, timings
