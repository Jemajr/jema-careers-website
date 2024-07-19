import pymysql
import os


def get_jobs():
  timeout = 10
  connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="defaultdb",
    host=os.environ['DB_HOST'],
    password=os.environ['DB_PASSWORD'],
    read_timeout=timeout,
    port=int(os.environ['DB_PORT']),
    user="avnadmin",
    write_timeout=timeout,
  )
  
  try:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM jobs")
    result = cursor.fetchall()
    #print(result)
  finally:
    connection.close()
  return result

#print(get_jobs())