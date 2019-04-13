from flask import Flask, render_template
app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
	return render_template("home.html")

@app.route('/meme/<meme_name>')
def meme(meme_name):
	return f'This is where the {meme_name} goes, yo.'