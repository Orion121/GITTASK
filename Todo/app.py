from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

client = MongoClient(MONGO_URI)
db = client['FlaskDb']
todo_collection = db["items"]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')
    
    if not item_name or not item_description:
        return jsonify({'error': 'Missing required fields'}), 400
    
    todo_collection.insert_one({"itemName": item_name, "itemDescription": item_description})
    return jsonify({'message': 'Item added successfully'})

if __name__ == '__main__':
    app.run(debug=True, port=5002)
