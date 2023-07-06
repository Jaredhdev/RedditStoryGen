from flask import Flask, request, jsonify, send_file, url_for
from video import get_link
import uuid
import shutil
import os
import csv

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

    link = get_link(f"{unique_id}.mp4")
    print(link)
    return link
