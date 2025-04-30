from django.db import models
import oracledb as db
from web import models
# 사이버다임
def foodListData(page):
    try:
        conn=models.getConnection()
        cur=conn.cursor()
        rowSize=12
        start=(rowSize*page)-(rowSize-1)
        end=rowSize*page
        sql= f"""
             SELECT fno,name,poster,num 
             FROM (SELECT fno,name,poster,rownum as num
             FROM (SELECT /*+ INDEX_ASC(project_food pf_fno_pk)*/fno,name,poster
             FROM project_food))
             WHERE num BETWEEN {start} AND {end}
             """
        cur.execute(sql)
        food_list=cur.fetchall()
        '''
          fetchone = (....)
          fetchall =[(),(),()..]
        '''
        cur.close()
        cur=conn.cursor()
        sql="""
            SELECT CEIL(COUNT(*)/12.0) 
            FROM project_food
            """
        cur.execute(sql)
        total=cur.fetchone() #(100,)
    except Exception as e:
          print(e)
    finally:
        models.disConnection(conn,cur)

    return food_list,total[0]
def foodDetailData(fno):
    try:
        conn=models.getConnection()
        cur=conn.cursor()
        sql=f"""
            SELECT fno,name,poster,address,phone,
                   time,theme,content,type,parking
            FROM project_food
            WHERE fno={fno}
            """
        cur.execute(sql)
        food_detail=cur.fetchone()
    except Exception as e:
        print(e)
    finally:
        models.disConnection(conn,cur)

    return food_detail

