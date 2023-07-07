from flask import Flask, request, jsonify, send_file, url_for
import uuid
import shutil
import os

from text import create_images, create_title_img
from overlay import compose_video
from tts import text_to_speech
from video import download_video

app = Flask(__name__)


@app.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':
        data = request.json
        title = data['title']
        text = data['text']

        download_video()
        unique_id = str(uuid.uuid4())
        dir_path = './' + unique_id
        os.makedirs(dir_path)

        text_to_speech(title, f'{dir_path}/title.mpeg')
        words, times = text_to_speech(text, f'{dir_path}/text.mpeg')
        create_title_img(title, dir_path)
        create_images(words, dir_path)
        compose_video(dir_path, times)

        response = {
            'success': True,
            'message': 'Video Generated',
            'unique_id': unique_id,  # Send unique_id to user
            'download_url': url_for('getvideo', unique_id=unique_id, _external=True)  # Sending back the full URL
        }
        print(response)
        return jsonify(response), 200


@app.route('/getvideo/<unique_id>', methods=['GET'])
def getvideo(unique_id):
    # Using the unique_id to determine file path
    video_path = f'./userdirs/{unique_id}/output.mp4'

    return send_file(video_path, mimetype='video/mp4', as_attachment=True)
