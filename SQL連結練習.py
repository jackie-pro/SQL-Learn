# -*- coding: utf-8 -*-
"""
Created on Thu May 14 16:55:10 2020

@author: Jackie
"""

#連資料庫檔
import sqlite3

#建立資料庫連結
conn = sqlite3.connect('students.db') #放跟.py同一個位置
#conn = sqlite3.connect('C:\code\sql\SQL-Learn\students.db')
#conn = sqlite3.connect(r'C:\code\sql\SQL-Learn\students.db')
#執行SQL指令SELECT
cursor = conn.execute('SELECT * FROM students')
#取出查詢結果的每一筆紀錄
for row in cursor:

        print(row[1], row[2], row[6])    
conn.close() #關閉資料庫
#================================================
#練習
import sqlite3

#建立資料庫連結
#conn = sqlite3.connect('students.db') #放跟.py同一個位置
conn = sqlite3.connect('C:\code\sql\SQL-Learn\students.db')
#conn = sqlite3.connect(r'C:\code\sql\SQL-Learn\students.db')
#執行SQL指令SELECT
cursor = conn.execute('SELECT * FROM Students')
#取出查詢結果的每一筆紀錄
for row in cursor:
        print(row[1], row[2],row[6])    
conn.close() #關閉資料庫

#================================================
#練習
import sqlite3

#建立資料庫連結
#conn = sqlite3.connect('csvtest.db') #放跟.py同一個位置
conn = sqlite3.connect('C:\code\sql\SQL-Learn\csvtest.db')
#conn = sqlite3.connect(r'C:\code\sql\SQL-Learn\csvtest.db')
#執行SQL指令SELECT
cursor = conn.execute('SELECT * FROM csvsample')
#取出查詢結果的每一筆紀錄
for row in cursor:
        print(row[0], row[1],row[2])    
conn.close() #關閉資料庫

#================================================
#20200518
import sqlite3

book = "P0004,SQL資料庫,520"
f = book.split(",")

#建立資料庫連接 => 如無資料庫 則建立資料庫
conn = sqlite3.connect("Books1.db")
#conn = sqlite3.connect('C:\code\sql\SQL-Learn\Books1.db')
#建立SQL指令CREATE字串 => 建資料表
#Books = "CREATE TABLE Books (id varchar(255), title varchar(255), price int(20))" 
#Create = conn.execute(Books)
#建立SQL指令INSERT字串
#sql = "INSERT INTO Books (id, title, price) VALUES ('{0}','{1}', '{2}')".format(f[0], f[1], f[2])
sql = "INSERT INTO Books (id, title, price) VALUES ('{0}','{1}', '{2}')"
sql = sql.format(f[0], f[1], f[2])
print(sql)
Insert = conn.execute(sql) #執行SQL指令
print(Insert.rowcount)
conn.commit() #確認交易
conn.close() #關閉資料庫連結
#================================================
#練習-持續輸入
import sqlite3
def icof(a, b, c):
    book = ("%s,%s,%s" % (a,b,c))
    f = book.split(",")
    conn = sqlite3.connect("Books1.db")
    sql = "INSERT INTO Books (id, title, price) VALUES ('{0}','{1}', '{2}')"
    sql = sql.format(f[0], f[1], f[2])
    conn.execute(sql) 
    conn.commit() 
    conn.close()   
print("已進入書籍資料建立系統。")
d = input("是否要開始輸入書籍資料(Y/N):")

while d.upper() == "Y":
    a = input("請輸入書籍資料(編號):")
    b = input("請輸入書籍資料(書名):")
    c = input("請輸入書籍資料(價格):")
    icof(a, b, c)
    print("已完成書籍資料建立。")
    d = input("是否要繼續輸入(Y/N):")
else:
   print("已離開書籍資料輸入系統。")
        
#================================================
#連MySQL 查詢
import pymysql
#建立資料庫連接
db = pymysql.connect("localhost", "root", "jackie1234", "aaa", charset="utf8")
cur = db.cursor() #建立cur物件
#執行SQL指令SELECT
cur.execute("SELECT * FROM students")
data = cur.fetchall()  #取出所有資料
#取出查詢結果的每一筆紀錄
for row in data:
    print(row[0], row[1], row[2], row[6]) #列出需要的欄位
db.close() #關閉資料庫連接

#================================================
#連MySQL 輸入資料
import pymysql

book = "P0004,Python程式設計,g,550,程式設計,2018-01-01"
f = book.split(",")

#建立資料庫連接    
db = pymysql.connect("localhost", "root", "jackie1234", "abc", charset="utf8")
cur = db.cursor() #建立cur物件
#建立SQL指令INSTER字串 
sql = "INSERT INTO books (id,title,author,price,category,pubdate) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')"
sql = sql.format(f[0], f[1], f[2], f[3], f[4], f[5])
print(sql)
try:
    cur.execute(sql)  #執行SQL指令
    db.commit()  #確認交易
    print("新增一筆紀錄...")
except:
    db.rollback()  #回復交易
    print("新增紀錄失敗...")
db.close()  #關閉資料庫連接

#================================================
#練習-持續輸入
import pymysql

def icof(a, b, c, d, e, f):
    book = ("%s,%s,%s,%s,%s,%s" % (a,b,c,d,e,f))
    z = book.split(",")
    db = pymysql.connect("localhost", "root", "jackie1234", "abc", charset="utf8")
    cur = db.cursor() #建立cur物件
    sql = "INSERT INTO books (id,title,author,price,category,pubdate) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')"
    sql = sql.format(z[0], z[1], z[2], z[3], z[4], z[5])
    try:
        cur.execute(sql)  #執行SQL指令
        db.commit()  #確認交易
        print("新增一筆紀錄...")
    except:
        db.rollback()  #回復交易
        print("新增紀錄失敗...")
    db.close()  #關閉資料庫連接
        
print("已進入書籍資料建立系統。")
x = input("是否要開始輸入書籍資料(Y/N):")

while x.upper() == "Y":
    a = input("請輸入書籍資料(編號):")
    b = input("請輸入書籍資料(書名):")
    c = input("請輸入書籍資料(作者):")
    d = input("請輸入書籍資料(價格):")
    e = input("請輸入書籍資料(類型):")
    f = input("請輸入書籍資料(出版日期 ex: 2018-01-01):")
    icof(a, b, c, d, e, f)
    print("已完成書籍資料建立。")
    x = input("是否要繼續輸入(Y/N):")
else:
   print("已離開書籍資料輸入系統。")

#====================================
import pymysql
#建立資料庫連接
db = pymysql.connect("localhost", "root", "jackie1234", "abc", charset="utf8")
cur = db.cursor() #建立cur物件
#執行SQL指令SELECT
cur.execute("SELECT Min(price) FROM books")
data = cur.fetchall()  #取出所有資料
for row in data:
    print('%d' % row[0])
#取出查詢結果的每一筆紀錄
#for row in data:
#    print(row[0], row[1], row[2], row[6]) #列出需要的欄位
#for row in data:
#   print(row[0])
db.close() #關閉資料庫連接