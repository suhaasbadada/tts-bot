from flask import Flask, render_template, request
from gtts import gTTS

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def speak():
    if request.method == "POST":
        text = request.form["text"]
        # Convert text to speech using gTTS
        tts = gTTS(text=text, lang="en")
        try:
            # Option 1 (preferred): Use get_bytes if available (updated gTTS)
            audio_data = tts.get_bytes()
            with open("temp.mp3", "wb") as f:
                f.write(audio_data)
        except AttributeError:
            # Option 2 (fallback): Use save method for older gTTS versions
            tts.save("temp.mp3")
        # Display success message with optional audio download link
        return f"Text converted to speech: {text} <br> <a href='/temp.mp3'>Download Audio</a>"
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
