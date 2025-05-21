from flask import Flask, jsonify, render_template, request
from datetime import datetime
import re
from flask_cors import CORS
import pyodbc

app = Flask(__name__, template_folder='templates')
CORS(app)

# Opretter forbindelsesstreng til SQL Server
connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=mssql7.unoeuro.com,1433;"
    "DATABASE=elkg_dk_db_login_service;"
    "UID=elkg_dk;"
    "PWD=wyxhd4RzcBpfk9G6gAHm;"
)

@app.route('/')
def index():
    # Viser forsiden
    return render_template('index.html')

@app.route('/indtast-pin')
def indtast_pin():
    # Viser pinkode-indtastningssiden
    return render_template('indtastpin.html')

@app.route('/validate-pin', methods=['POST'])
def validate_pin():
    # Modtager og validerer pinkode fra bruger
    data = request.get_json()
    pincode = data.get('pincode', '')
    # Tjek at pinkoden er præcis 4 cifre
    if not re.fullmatch(r'\d{4}', pincode):
        return jsonify({"success": False, "message": "Pinkoden skal være 4 cifre."}), 400

    conn = None
    try:
        # Opretter forbindelse til databasen
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        # Tjekker om pinkoden findes i dagens booking og tidsinterval
        query =  """
            SELECT COUNT(*) FROM Booking 
            WHERE LTRIM(RTRIM(PinCode)) = ? 
            AND CAST(Date AS DATE) = CAST(GETDATE() AS DATE) 
            AND CAST(Starttime AS TIME) <= CAST(GETDATE() AS TIME) 
            AND CAST(Endtime AS TIME) >= CAST(GETDATE() AS TIME)
            """
        cursor.execute(query, (pincode,))
        result = cursor.fetchone()
    except Exception as e:
        # Fejl ved databaseforbindelse
        return jsonify({"success": False, "message": f"Database error: {str(e)}"}), 500
    finally:
        # Lukker forbindelsen hvis den er åben
        if conn:
            conn.close()

    # Returnerer succes hvis pinkoden findes, ellers fejl
    if result and result[0] > 0:
        return jsonify({"success": True, "message": "Pinkoden er korrekt."})
    else:
        return jsonify({"success": False, "message": "Forkert pinkode."}), 401


if __name__ == '__main__':
    # Starter Flask-serveren
    app.run(host='0.0.0.0', port=8000)