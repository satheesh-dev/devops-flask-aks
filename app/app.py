from flask import Flask
import random
import os

app = Flask(__name__)

@app.route("/")
def home():
    greeting = os.getenv("GREETING", "Hello")
    return f"🚀 {greeting} from Flask DevOps App! rightu"

@app.route("/health")
def health():
    return "OK", 200

@app.route("/crash")
def crash():
    if random.random() > 0.5:
        return "Simulated crash", 500
    return "All good", 200

@app.route("/metrics")
def metrics():
    return "requests_total 1\n", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
