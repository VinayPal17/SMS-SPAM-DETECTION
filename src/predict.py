import pickle
from src.preprocessing import preprocess_text

# Load vectorizer
with open("model/vectorizer.pkl","rb") as file:
    vectorizer = pickle.load(file)


# Load trained model
with open("model/spam_model.pkl","rb") as file:
    model = pickle.load(file) 


def predict_spam(message):

    transformed_message = preprocess_text(message)

    vector = vectorizer.transform([transformed_message])

    prediction = model.predict(vector)[0]

    probabilities = model.predict_proba(vector)[0]

    confidence = max(probabilities) * 100

    result = "SPAM" if prediction == 1 else "HAM"

    return result, round(confidence, 2)
