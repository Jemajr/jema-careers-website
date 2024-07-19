from flask import Flask, render_template, jsonify
from main import get_jobs, fetch_job


app = Flask(__name__, static_folder='static')


@app.route("/")
def hello_world():
  JOBS = get_jobs()
  return render_template('home.html',
                        jobs = JOBS)


@app.route("/api/jobs")
def list_jobs():
  JOBS = get_jobs()
  return jsonify(JOBS)


@app.route("/job/<id>")
def show_job(id):
  JOB = fetch_job(id)
  if not JOB:
    return "Not Found", 404
  return render_template('jobpage.html',
                        job = JOB)
  #return jsonify(job)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)