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
    
  finally:
    connection.close()
    
  return result

def fetch_job(id):
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
    cursor.execute("SELECT * FROM jobs WHERE id = %s", (id))
    result = cursor.fetchall()
    
  finally:
    connection.close()

  print(result[0])
  if len(result) == 0:
    return None
  else: 
    return result[0]
fetch_job(4)