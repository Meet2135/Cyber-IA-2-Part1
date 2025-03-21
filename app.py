from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the simple Flask web service!"})

@app.route('/status')
def status():
    return jsonify({"status": "Service is running", "uptime": "24/7"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
