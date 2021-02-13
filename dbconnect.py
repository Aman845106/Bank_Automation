import pymysql as sql
def getCon():
    con=sql.connect(host='localhost',password='root',user='root',database='mybank',port=3306)
    return con
