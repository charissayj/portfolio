from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/projects-technologies')
def projectsTech():
	return render_template('projects-technologies.html')

@app.route('/projects')
def projects():
	return render_template('projects-technologies.html')

@app.route('/about')
def about():
	return render_template('about-charissa.html')

@app.route('/education')
def education():
	return render_template('education.html')

app.run(debug=True)