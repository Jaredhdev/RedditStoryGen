from flask import Flask, request, jsonify, send_file

from text import create_images, create_title_img
from overlay import compose_video
from tts import text_to_speech

app = Flask(__name__)


@app.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':
        data = request.json
        title = data['title']
        text = data['text']

        text_to_speech(title, './audio/title.mpeg')
        words, times = text_to_speech(text, './audio/output.mpeg')

        images_folder = './images'
        create_title_img(title, images_folder)
        create_images(words, images_folder)

        compose_video('./videos/Gameplay15.mp4', './audio/output.mpeg', './audio/title.mpeg', images_folder, times,
                      './output')

        # return the name of the file or any response you want
        return jsonify({'success': True, 'message': 'Generate Completed'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
