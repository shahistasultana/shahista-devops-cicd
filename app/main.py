from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "Shahista DevOps Monitoring App",
        "message": "Welcome to our DevOps project",
        "status": "running",
        "version": "1.0.0"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "DevOps Monitoring App"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
