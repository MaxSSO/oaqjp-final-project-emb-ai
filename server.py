from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Sentiment Analyzer")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotion():
    text = request.args.get('textToAnalyze')
    emotions = emotion_detector(text)
    return f"For the given statement, the system response is 'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, 'joy': {emotions['joy']} and 'sadness': {emotions['sadness']}. The dominant emotion is {emotions['dominant_emotion']}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
