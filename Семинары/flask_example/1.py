from flask import Flask
from flask import url_for, render_template, request, redirect

app = Flask(__name__)

@app.route('/poem')
def index():
	with open("poem.txt", "r", encoding='utf-8') as f:
		content = f.read()
	return render_template("poem.html", content=content)

if __name__ == '__main__':
	app.run(debug=True)