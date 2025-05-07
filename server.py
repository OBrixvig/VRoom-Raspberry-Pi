from flask import Flask, jsonify, render_template
from datetime import datetime

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-in', methods=['POST'])
def check_in():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({"message": f"Checked in at {current_time}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)