# import module containing all directory info
from settings import configure_directories
configure_directories()
from userroute import user_routes
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from flask import Flask, jsonify
import psycopg2
app = Flask(__name__)
user_routes(app)

@app.route('/')
def home():
	return jsonify(message='welcome to my first python-sql powered api',
		status='ok'
		)
if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=ewTrue)