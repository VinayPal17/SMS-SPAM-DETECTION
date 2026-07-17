from flask import Flask,render_template,request
from src.predict import predict_spam


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    message = request.form["message"]

    prediction, confidence = predict_spam(message)

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        message=message
    )



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)    