from flask import request, jsonify
import os
import psycopg2

def signup():
	db = psycopg2.connect(dbname=os.environ.get('DBNAME'), user=os.environ.get('DBNAME'), host=os.environ.get('DBHOST'),password=os.environ.get('DBPASSWORD'))
	cur = db.cursor()
	cur.execute('CREATE TABLE users (id serial PRIMARY KEY, firstname varchar, lastname varchar, role varchar);')
	cur.execute('INSERT INTO users (firstname, lastname, role) VALUES(%s, %s, %s)',
		('efosa', 'okpugie', 'user'))
	db.commit()
	cur.close()
	db.close()
	return jsonify(message='Successfully signed up'), 201
		
		
