# import module containing all directory info
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from flask import Flask, jsonify
import psycopg2
app = Flask(__name__)

db = psycopg2.connect(dbname=os.environ.get('DBNAME'), user=os.environ.get('DBNAME'), host=os.environ.get('DBHOST'),password=os.environ.get('DBPASSWORD'))
@app.route('/')
def home():
	return jsonify(message='welcome to my first python-sql powered api',
		status='ok'
		)
if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)