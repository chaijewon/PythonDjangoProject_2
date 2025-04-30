from django.db import models
# 데이터베이스 연동
# Create your models here.
import oracledb as db
import os
import sys
import urllib.request
import json
# 데이터베이스 연결
def getConnection():
    try:
        '''
        conn=db.connect(user="hr",
                    password="happy",
                    dsn="localhost:1521/XE")
        '''
        conn=db.connect("hr/happy@localhost:1521/XE")
    except Exception as e:
           print(e)
    return conn
def disConnection(conn,cur):
    try:
         cur.close()
         conn.close()
    except Exception as e:
         print(e)
def mainData():
    try:
        conn=getConnection()
        cur=conn.cursor()
        sql="""
             SELECT no,title,poster,chef,rownum 
             FROM (SELECT no,title,poster,chef
                   FROM recipe ORDER BY no ASC)
             WHERE rownum<=12
            """
        cur.execute(sql)
        recipe_list=cur.fetchall()
        cur.close()

        cur=conn.cursor()
        sql = """
                 SELECT fno,name,poster,rownum 
                 FROM (SELECT fno,name,poster
                       FROM project_food ORDER BY fno ASC)
                 WHERE rownum<=12
                """
        cur.execute(sql)
        food_list=cur.fetchall()
    except Exception as e:
          print(e)
    finally:
        disConnection(conn,cur)

    return recipe_list,food_list



