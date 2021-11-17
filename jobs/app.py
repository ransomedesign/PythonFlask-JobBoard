from flask import Flask
from flask import render_template

app = Flask(__name__)

# Route for showing jobs.


@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
