from flask import Flask, jsonify, render_template, request
from datetime import datetime
import re
from flask_cors import CORS
import pyodbc

app = Flask(__name__, template_folder='templates')
CORS(app)

connection_string = pyodbc.connect("Server=mssql7.unoeuro.com,1433;Database=elkg_dk_db_login_service;User Id=elkg_dk;Password=wyxhd4RzcBpfk9G6gAHm;")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/indtast-pin')
def indtast_pin():
    return render_template('indtastpin.html')

@app.route('/validate-pin', methods=['POST'])
def validate_pin():
    data = request.get_json()
    pincode = data.get('pincode', '')
    if not re.fullmatch(r'\d{4}', pincode):
        return jsonify({"success": False, "message": "Pincode must be 4 digits."}), 400

    conn = None
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM Booking WHERE PinCode = ? and Date =CONVERT(DATE, GETDATE()) AND Starttime <= convert(TIME, GETDATE()) AND Endtime >= convert(TIME, GETDATE())"
        cursor.execute(query, (pincode,))
        result = cursor.fetchone()
    except Exception as e:
        return jsonify({"success": False, "message": f"Database error: {str(e)}"}), 500
    finally:
        if conn:
            conn.close()

    if result and result[0] > 0:
        return jsonify({"success": True, "message": "Pincode is korrekt."})
    else:
        return jsonify({"success": False, "message": "Incorrect pincode."}), 401
    



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)