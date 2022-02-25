import Utils
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def score_server():
 score = open(SCORES_FILE_NAME, "r").read()
 try:
  return render_template('show_score.html', score=score)
 except Exception as e:
  print(e)
  return render_template('score_problem.html', error=BAD_RETURN_CODE)


def shutdown_server():
 func = request.environ.get('werkzeug.server.shutdown')
 if func is None:
  raise RuntimeError('Not running with the Werkzeug Server')
 func()

if __name__ == "__main__":
 app.run(host='0.0.0.0', port=8777)
