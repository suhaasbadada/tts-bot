from flask import Flask, render_template, request, send_file
from gtts import gTTS
from io import BytesIO
from utils import apply_time_stretching

app = Flask(__name__)

@app.route("/api/speak/gtts", methods=["POST"])
def speak_gtts():
    if request.method == "POST":
        try:
            text = request.json["text"]
        except KeyError:
            return "Missing 'text' key in request body", 400

        tts = gTTS(text=text, lang="en",slow=False) # text to speech using gTTS

        # storing audio in memory
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)

        # faster_file=apply_time_stretching(audio_bytes.read(),1.5)
        # returning audio file
        return send_file(
            audio_bytes,
            download_name="gtts_speech.mp3",
            mimetype="audio/mp3",
            as_attachment=True
        )

if __name__ == "__main__":
    app.run(debug=True)
