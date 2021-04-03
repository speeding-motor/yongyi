# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pickle
import math
import time
import numpy as np
import pymysql
import mysql.connector


#
# con = mysql.connector.connect(user='root', password='rootroot',
#                               host='127.0.0.1',
#                               database='xrk')
# con.close()

config = {
    'user': 'root',
    'password': 'rootroot',
    'host': '127.0.0.1',
    'database': 'xrk',
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cursor = cnx.cursor()
# query = "select * from users"
# for (id, name, phone_num) in cursor:
#   print("id={}, name={} , phone_num={}".format(id, name, phone_num))
name = 'xxxx'
phone_num = 18210827069
add_user = "insert into  xrk.users(name, phone_num) values(%s, %s)"

# add_employee = ("INSERT INTO employees "
#                 "(first_name, last_name, hire_date, gender, birth_date) "
#                 "VALUES (%s, %s, %s, %s, %s)")

cursor.execute(add_user, (name, phone_num))
cnx.commit()
cursor.close()
cnx.close()
