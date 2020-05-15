# -*- coding: utf-8 -*-
"""
Created on Thu May 14 16:55:10 2020

@author: Jackie
"""


import sqlite3

#建立資料庫連結
conn = sqlite3.connect('students.db') #放跟.py同一個位置
#conn = sqlite3.connect('C:\\TEMP\\聯成-程式課\\上課資料\\SQL\\練習\\students.db')
#conn = sqlite3.connect(r'C:\TEMP\聯成-程式課\上課資料\SQL\練習\students.db')
#執行SQL指令SELECT
cursor = conn.execute('SELECT * FROM Students')
#取出查詢結果的每一筆紀錄
for row in cursor:

        print(row[1], row[2], row[6])    
conn.close() #關閉資料庫
#================================================
import sqlite3

#建立資料庫連結
conn = sqlite3.connect('students.db') #放跟.py同一個位置
#執行SQL指令SELECT
cursor = conn.execute("SELECT * FROM Students WHERE csex = 'F'")
#取出查詢結果的每一筆紀錄
for row in cursor:
        print(row[1], row[2], row[6])    
conn.close() #關閉資料庫