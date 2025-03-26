from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/log', methods=['POST'])
def log_action():
    data = request.get_json()
    name = data.get("name", "neznámý")
    action = data.get("action", "neznámá akce")
    timestamp = data.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    entry = f"{timestamp} | {name} | {action}\n"
    with open("zaznamy.txt", "a", encoding="utf-8") as f:
        f.write(entry)

    return {"status": "ok"}
