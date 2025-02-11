# app.py
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"message": "server is up and running"})

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)

