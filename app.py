from flask import Flask, render_template, request
import reddit_switch_script as switch
import reddit_game_scraper as games
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
	return render_template("index.html")

@app.route("/game-search", methods=["POST"])
def game_search():
	name = request.form.get("lastname")
	deals = games.run(name)
	return render_template("index.html", query=True, game=True, posts=deals)
@app.route("/switch")
def switch_deals():
	packet = switch.run()
	return render_template("index.html", query=True, game=False, posts=packet)
if __name__ == '__main__':
	app.run()
