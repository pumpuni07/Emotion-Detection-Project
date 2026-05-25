"""
Flask web server for the Emotion Detection application.

Serves the front-end and exposes the /emotionDetector endpoint
which processes text input and returns formatted emotion analysis results.
"""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the main index page of the Emotion Detection application."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Analyze the emotion of the provided text and return a formatted response.

    Query Parameters:
        textToAnalyze (str): The text input from the user to be analyzed.

    Returns:
        str: A formatted string describing the emotion scores and dominant emotion,
             or an error message if the input is blank or invalid.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )
    return response_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
