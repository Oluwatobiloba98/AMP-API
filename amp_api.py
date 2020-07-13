from flask import Flask, render_template, url_for
app = Flask(__name__)

updates = [{
	'author' : 'AMP_API',
	'title' : 'Welcome',
	'content' : 'You are welcome to this antimicrobial peptide prediction API',
	'date_posted' : 'July 7, 2020'
}]
@app.route("/")
@app.route("/Home")
def home():
	return render_template('home.html', posts = updates)

@app.route("/about")

def about():
	return render_template('about.html', title = 'About')


if __name__ == '__main__':
	app.run(debug=True)
