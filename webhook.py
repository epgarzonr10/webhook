from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route('/webhook', methods=['POST'])
def webhook():
    event_data = request.json

    print("Webhook received:", event_data)

    return jsonify({"message": "Webhook received successfully"}), 200

if __name__ == '__main__':
    app.run(port=5000)
