from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

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
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE registration_number=? AND password=?", (reg, pwd))
    row = cursor.fetchone()
    conn.close()

    if row:
        student = {
            "id": row[0],
            "registration_number": row[1],
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

# ✅ عرض index.html عند زيارة /
@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

# ✅ عرض أي ملف ثابت داخل مجلد static/
@app.route('/<path:path>')
def serve_static_file(path):
    return send_from_directory('static', path)

# ✅ تشغيل التطبيق على المنفذ الصحيح
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

