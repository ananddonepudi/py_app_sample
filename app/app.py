
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hello from AWS CodeBuild!")

if __name__ == "__main__":
    if os.environ.get("RUN_SERVER") == "true":
        app.run(host="0.0.0.0", port=5000)
    else:
        print("Build check: Flask app loaded successfully.")

