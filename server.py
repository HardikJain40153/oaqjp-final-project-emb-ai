""" Module to act as a server for Flask web deployment of EmotionDetection application """

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detection")

@app.route("/emotionDetector")
def get_emotion_detector_response():
    """ Call emotion_detector API and get response based on input received """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (f"For the given statement, the system response is "
            f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, 'joy': {response['joy']} "
            f"and 'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}.")

@app.route("/")
def render_html_page():
    """ Root index.html page """
    return render_template("index.html")

app.run(host = "0.0.0.0", port = 5000)
