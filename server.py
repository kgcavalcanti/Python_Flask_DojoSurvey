from flask import Flask, render_template, redirect, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']
    print request.form
    return render_template('summary.html', name = name, location = location, language = language, comments = comments)

app.run(debug=True)
