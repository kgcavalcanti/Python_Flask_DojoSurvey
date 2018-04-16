from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'fauiwefj09a3458390458'

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
	session['name'] = request.form['name']
	session['location'] = request.form['location']
	session['language'] = request.form['language']
	session['comments'] = request.form['comments']
	if len(session['name']) < 1 or len(session['comments']) < 1:
		flash("Name or comments cannot be empty!")
		return redirect('/')
	else:
		return render_template('summary.html')

 
app.run(debug=True)
