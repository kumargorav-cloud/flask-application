from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "this is my first flask application"

@app.route("/htmlfile")
def htmlfile():
    return render_template('first.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=3000,debug=True)

