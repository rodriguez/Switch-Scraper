from flask import Flask, render_template
import reddit_switch_web_script.py

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
        app.run()
