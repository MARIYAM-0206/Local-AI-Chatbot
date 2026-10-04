from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:1.5b"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"response": "Please enter a message."})

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": message,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()
        result = response.json()

        return jsonify({"response": result["response"]})

    except requests.exceptions.RequestException as e:
        return jsonify({
            "response": f"Could not connect to Ollama: {e}"
        }), 500


if __name__ == "__main__":
    app.run(debug=True)