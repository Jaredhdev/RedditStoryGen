from flask import Flask, request, jsonify, send_file, url_for
import uuid
import shutil
import os

from tasks import process_video

app = Flask(__name__)


@app.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':
        data = request.json
        title = data['title']
        text = data['text']

        unique_id = str(uuid.uuid4())

        process_video.delay(title, text, unique_id)

        response = {
            'success': True,
            'message': 'Video Generation Job Enqueued',
            'job_id': unique_id
        }

        return jsonify(response), 200


@app.route('/getvideo/<unique_id>', methods=['GET'])
def getvideo(unique_id):
    # Using the unique_id to determine file path
    video_path = f'./{unique_id}/output.mp4'

    return send_file(video_path, mimetype='video/mp4', as_attachment=True)
