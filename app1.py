#!/usr/bin/env python
# coding: utf-8

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import mysql.connector
import pandas as pd
import datetime
import os
import traceback

app = Flask(__name__)
CORS(app)

REPORTS_DIR = "reports"
os.makedirs(REPORTS_DIR, exist_ok=True)  # Ensure reports directory exists

# Function to establish a database connection
def get_db_connection():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="aneesh25",  # Use environment variable
            database="MessMenuDB",
            use_pure=True
        )
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None

# Route to insert student & mess details
@app.route('/submit', methods=['POST'])
def submit():
    data = request.json  # Receive data from React
    print("Received data:", data)  # Debugging log

    if not data or 'student' not in data or 'mess' not in data:
        return jsonify({"error": "Invalid request: missing student or mess data"}), 400  

    student = data['student']
    mess = data['mess']
    source = data.get("source", "unknown")  # Identifying which button triggered the request

    if 'regNo' not in student or not student['regNo']:
        return jsonify({"error": "Invalid request: regNo is missing in student data"}), 400

    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        with conn.cursor() as cursor:
            # Insert into Students table
            sql_students = """
            INSERT IGNORE INTO Students (reg_no, name, block, room_number) 
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql_students, (student['regNo'], student['name'], student['block'], student['roomNumber']))

            # Insert into MessDetails table
            sql_mess = """
            INSERT INTO MessDetails (reg_no, mess_name, mess_type, food_suggestion, meal_type, feasibility)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql_mess, (
                student['regNo'], mess['messName'], mess['messType'], 
                mess['foodSuggestion'], mess['mealType'], mess['feasibility']
            ))

            conn.commit()
            print(f"Data Inserted Successfully from {source} button")
            return jsonify({"message": "Data Inserted Successfully!", "source": source})

    except mysql.connector.Error as e:
        conn.rollback()
        print(f"MySQL Error: {e}")
        print(traceback.format_exc())  # Print full error traceback
        return jsonify({"error": "Database error", "details": str(e)}), 500

# Route to generate Excel report based on filters
@app.route('/generate-report', methods=['POST'])
def generate_report():
    filters = request.json
    print("Received filters:", filters)  # Debugging log

    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        with conn.cursor() as cursor:
            query = """
            SELECT reg_no, mess_name, mess_type, food_suggestion, meal_type, feasibility 
            FROM MessDetails WHERE 1=1
            """
            params = []

            if 'regNo' in filters and filters['regNo']:
                query += " AND reg_no LIKE %s"
                params.append(filters['regNo'] + "%")

            cursor.execute(query, params)
            data = cursor.fetchall()

            if not data:
                return jsonify({"message": "No records found for the given filters"}), 404

            print(f"Fetched {len(data)} rows")  # Debug log

            df = pd.DataFrame(data, columns=["Reg No", "Mess Name", "Mess Type", "Food Suggestion", "Meal Type", "Feasibility"])
            
            filename = f"MessReport_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
            file_path = os.path.join(REPORTS_DIR, filename)
            df.to_excel(file_path, index=False)

            print("Report Generated:", filename)
            return jsonify({
                "message": "Report Generated!",
                "file_url": f"http://127.0.0.1:5000/download-report/{filename}"
            })

    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
        return jsonify({"error": "Database error", "details": str(e)}), 500

    finally:
        conn.close()

# Route to serve the generated report
@app.route('/download-report/<filename>', methods=['GET'])
def download_report(filename):
    try:
        return send_from_directory(REPORTS_DIR, filename, as_attachment=True)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
