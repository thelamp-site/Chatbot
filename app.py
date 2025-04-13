from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import chat_response

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "RahulBot is Alive!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    if not message:
        return jsonify({"reply": "Kuch toh likh bhai!"})
    reply = chat_response(message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
