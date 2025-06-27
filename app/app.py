
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hello from AWS CodeBuild + Terraform Pipeline!")

if __name__ == "__main__":
       print("Hello from AWS CodeBuild! No server started.")
