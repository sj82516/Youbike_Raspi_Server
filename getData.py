#!/usr/bin/python
# -*- coding:utf8 -*-
#encoding = utf-8
import sqlite3
from datetime import datetime
import urllib2,json

conn = sqlite3.connect("/home/pi/youbike.db")
cursor = conn.cursor()

time = "A"+datetime.now().strftime('%Y%m%d')
time2 = datetime.now().strftime('%Y%m%d%H%M')
cursor.execute('CREATE TABLE if not exists {tn} (id TEXT,sna TEXT,tot TEXT,sbi TEXT,sarea TEXT,lat TEXT, lng TEXT,time TEXT)'.format(tn=time))
url = "http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=ddb80380-f1b3-4f8e-8016-7ed9cba571d5"
data = json.load(urllib2.urlopen(url))
for item in data['result']['results']:
	sql2 = "INSERT INTO %s VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (time,item['_id'],item['sna'],item['tot'],item['sbi'],item['sarea'],item['lat'],item['lng'],time2)
	cursor.execute(sql2)
conn.commit()
