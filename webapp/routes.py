from webapp import app
from flask import render_template


@app.route('/home', methods=['GET', 'POST'])
def home():
	return render_template('home.html')

@app.route('/view', methods=['GET', 'POST'])
def addthis():
	return f"{25 + 31}"