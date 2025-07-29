from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # ✅ تمكين CORS لكل المصادر

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    reg = data.get("registration_number")
    pwd = data.get("password")

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE registration_number=? AND password=?", (reg, pwd))
    row = cursor.fetchone()
    conn.close()

    if row:
        student = {
            "id": row[0],
            "registration_number": row[1],
            # "password": row[2],  # ❌ الأفضل حذفه لأسباب أمنية
            "full_name": row[3],
            "department": row[4],
            "year": row[5],
            "place": row[6],
            "birthdate": row[7],
            "photo_url": row[8]
        }
        return jsonify(student)
    else:
        return jsonify({"error": "Invalid credentials"}), 401

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # ✅ حتى يعمل على Render
    app.run(host='0.0.0.0', port=port)
