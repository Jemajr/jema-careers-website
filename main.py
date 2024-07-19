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

  if len(result) == 0:
    return None
  else: 
    return result[0]


def add_application_to_db(applicant_data, id):
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

    insert_query = """
    INSERT INTO job_applications 
    (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) 
    VALUES
    (%s, %s, %s, %s, %s, %s, %s)
    """
    
    job_id = id
    full_name = applicant_data['name']
    email = applicant_data['email']
    linkedin_url = applicant_data['linkedin_url']
    education = applicant_data['education']
    work_experience = applicant_data['work_experience']
    resume_url = applicant_data['resume_url']
    
    cursor.execute(insert_query, (job_id, full_name, email, linkedin_url, education, work_experience, resume_url))
    connection.commit()
    cursor.execute("SELECT * FROM job_applications")
    print(cursor.fetchall())
    
  finally:
    connection.close()


def clear_db():
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
    cursor.execute("DELETE FROM applications")
    connection.commit()
  finally:
    connection.close()

#clear_db()