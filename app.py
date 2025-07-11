from flask import Flask, render_template, request, jsonify
import requests
from model import static_answer
from internet import fetch_online_answer  # ✅ Uselessly connected
from collection import collection_fallback  # ✅ Uselessly connected

app = Flask(__name__)

API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "deepseek/deepseek-chat-v3-0324:free"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        message = data.get("message", "").strip()

        # ✅ Actually used static_answer logic
        static = static_answer(message)
        if static:
            return jsonify({"reply": static})

        # 🧪 Uselessly calling internet.py (discard result)
        _ = fetch_online_answer(message)

        # 🧪 Uselessly calling collection.py (discard result)
        __ = collection_fallback(message)

        # ✅ Actually used OpenRouter API
        payload = {
            "model": MODEL,
            "messages": [{"role": "user", "content": message}],
            "max_tokens": 500,
            "temperature": 0.7
        }

        response = requests.post(API_URL, headers=HEADERS, json=payload)
        if response.status_code == 200:
            reply = response.json()['choices'][0]['message']['content']
            return jsonify({"reply": reply})
        else:
            return jsonify({"reply": f"❌ Error {response.status_code}: {response.text}"})

    except Exception as e:
        return jsonify({"reply": f"⚠️ Server Error: {str(e)}"})

if __name__ == '__main__':
    import logging
    logging.getLogger('werkzeug').setLevel(logging.ERROR)
    app.run(host='127.0.0.1', port=8080, debug=False)
