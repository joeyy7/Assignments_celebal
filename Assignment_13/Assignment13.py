from flask import Flask, request, send_file
from gtts import gTTS
import os
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Text-to-Speech API!"

@app.route('/tts', methods=['POST'])
def text_to_speech():
    data = request.json
    text = data.get("text", "")
    
    if not text:
        return {"error": "No text provided"}, 400

    # Convert text to speech
    tts = gTTS(text)
    audio = BytesIO()
    tts.write_to_fp(audio)
    audio.seek(0)

    return send_file(audio, mimetype="audio/mpeg", as_attachment=True, download_name="output.mp3")

if __name__ == '__main__':
    app.run(debug=True)
