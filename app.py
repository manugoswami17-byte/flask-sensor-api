from flask import Flask, request, jsonify

app = Flask(__name__)
data_store = {}

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    data_store['latest'] = data
    return jsonify({"status": "received"}), 200

@app.route('/get', methods=['GET'])
def get():
    return jsonify(data_store.get('latest', {})), 200

@app.route('/', methods=['GET'])
def root():
    return "Sensor API is live.", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
