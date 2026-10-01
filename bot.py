from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "Wollo Exam Bot is running!"

def run():
    app.run(host="0.0.0.0", port=10000)

threading.Thread(target=run).start()

print("Wollo Exam Bot server started")
