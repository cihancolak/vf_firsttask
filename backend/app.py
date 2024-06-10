from flask import Flask, request, jsonify
import os
import mysql.connector
from mysql.connector import Error
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS'u tüm endpointler için etkinleştir

@app.route('/')
def hello():
    return jsonify(message="Hello from the backend!")

@app.route('/test_db_connection')
def test_db_connection():
    try:
        db = mysql.connector.connect(
            host=os.environ['DB_HOST'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            database=os.environ['DB_NAME']
        )
        if db.is_connected():
            return jsonify(message="Connected to the database"), 200
    except Error as e:
        return jsonify(error=str(e)), 500

@app.route('/data', methods=['GET', 'POST'])
def manage_data():
    try:
        db = mysql.connector.connect(
            host=os.environ['DB_HOST'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            database=os.environ['DB_NAME']
        )
        cursor = db.cursor()
        
        if request.method == 'POST':
            new_data = request.json.get('name')
            cursor.execute("INSERT INTO sample_table (name) VALUES (%s)", (new_data,))
            db.commit()
            return jsonify(message="Data added successfully"), 201
        
        cursor.execute("SELECT * FROM sample_table")
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return jsonify(data)
        
    except Error as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
