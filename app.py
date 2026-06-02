from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    return "Hello Ronit! Flask app deployed using CI/CD pipeline."

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)