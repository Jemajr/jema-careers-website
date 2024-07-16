from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder='static')

JOBS = [
  {
  'id': 1,
  'title': 'Data Engineer',
  'location': 'Seattle, WA',
  'salary': '$150,000'
  },
  {
  'id': 2,
  'title': 'Software Developer',
  'location': 'San Francisco, CA',
  'salary': '$180,000'
  },
  {
    'id': 3,
  'title': 'Marketing Manager',
  'location': 'New York, NY',
  'salary': '$120,000'
  },
  {
    'id': 4,
  'title': 'UX/UI Designer',
  'location': 'Austin, TX',
  'salary': '$130,000'
  },
  {
  'id': 5,
  'title': 'Financial Analyst',
  'location': 'Chicago, IL',
  'salary': '$110,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',
                        jobs = JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)