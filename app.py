from flask import Flask, render_template
import reddit_switch_script as switch

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
	return render_template("index.html")

@app.route("/<string:name>")
def game(name):
	name = switch.run()
	price = 50
	link = "www.google.com"
	return render_template("index.html", query=True, game=True, name=name, price=price, link=link)
@app.route("/switch")
def switch_deals():
	packet = switch.run()
	return render_template("index.html", query=True, game=False, posts=packet)
if __name__ == '__main__':
	app.run()
