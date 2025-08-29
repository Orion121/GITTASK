from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import os
from pymongo import MongoClient

app = Flask(__name__)

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

client = MongoClient(MONGO_URI)

db = client['FlaskDb']
collection = db['FlaskCollection']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        value = request.form.get('value')
        try:
            collection.insert_one({'name': name, 'value': value})
            return redirect(url_for('success'))
        except Exception as e:
            flash(f'Error: {str(e)}')
            
    all_data = list(collection.find())
    return render_template('form.html', all_data=all_data)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
