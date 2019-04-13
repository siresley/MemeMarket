from flask import Flask, render_template
from meme_url import urls

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
	return render_template("home.html", meme_url=meme_url.pepe_url)

@app.route('/meme/<meme_name>')
def meme(meme_name):
	meme_link = urls[meme_name]
	return render_template("home.html", meme_url=meme_link)

@app.route('/meme')
def create_meme():
	new_meme = Meme(name, image, source)