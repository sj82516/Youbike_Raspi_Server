# -*- coding:utf8 -*-
#encoding = utf-8
import sqlite3
import json
from flask import Flask,jsonify
from datetime import datetime,timedelta
import time

app = Flask(__name__)

@app.route("/<date>", methods=['GET'])
def hello(date):
	conn = sqlite3.connect("/home/pi/youbike.db")
	cursor = conn.cursor()
	sql = "select * from %s"%('A'+date)
	cursor.execute(sql)
	rows = cursor.fetchall()
	try:
		column = [t[0] for t in cursor.description]
		myresult = []
		for row in rows:
			myjson={column[0]:row[0], column[1]:row[1], column[2]:row[2], column[3]:row[3], column[4]:row[4]}
			myresult.append(myjson)
		json_result = json.dumps(myresult)
		return json_result
	except Exception as e:
		return str(e)
	return json_result

@app.route("/<date1>/<date2>", methods=['GET'])
def time(date1,date2):
	struct_date1 = datetime.strptime(date1,"%Y%m%d")
	struct_date2 = datetime.strptime(date2,"%Y%m%d")
	delta = timedelta(days=1)
	conn = sqlite3.connect("/home/pi/youbike.db")
	cursor = conn.cursor()
	myresult = []
	while struct_date1 <= struct_date2:
		sql="select * from %s"%('A'+datetime.strftime(struct_date1,'%Y%m%d'))
		cursor.execute(sql)
		rows = cursor.fetchall()
		column = [t[0] for t in cursor.description]
		for row in rows:
			myjson={column[0]:row[0], column[1]:row[1], column[2]:row[2], column[3]:row[3], column[4]:row[4]}
			myresult.append(myjson)
		struct_date1 = struct_date1 + delta
	try:
		json_result = json.dumps(myresult)
		return json_result
	except Exception as e:
		return str(e)

@app.route("/")
def index():
	return "Welcome"

if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0', port=8000,debug=True)
