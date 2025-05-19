from flask import Flask, jsonify, render_template, request
from datetime import datetime
import re

app = Flask(__name__, template_folder='templates')

# For demonstration, use a hardcoded pincode. Replace with DB lookup in production.
STORED_PINCODE = "1234"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-in', methods=['POST'])
def check_in():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({"message": f"Checked in at {current_time}"})

@app.route('/indtast-pin')
def indtast_pin():
    return render_template('indtastpin.html')

@app.route('/validate-pin', methods=['POST'])
def validate_pin():
    data = request.get_json()
    pincode = data.get('pincode', '')
    # Check if pincode is exactly 4 digits
    if re.fullmatch(r'\d{4}', pincode):
        if pincode == STORED_PINCODE:
            return jsonify({"success": True, "message": "Pincode is correct."})
        else:
            return jsonify({"success": False, "message": "Incorrect pincode."}), 401
    else:
        return jsonify({"success": False, "message": "Pincode must be 4 digits."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)