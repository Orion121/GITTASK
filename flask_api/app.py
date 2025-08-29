from flask import Flask, jsonify
import os, json

app = Flask(__name__)

@app.route('/api')
def get_list():
    data_file = os.path.join(os.path.dirname(__file__), 'data.json')
    with open(data_file, 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
