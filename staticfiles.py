from flask import Flask,render_template

app = Flask(__name__,static_folder='static',static_url_path='/')

@app.route("/")
def simple():
    return render_template('staticfile.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=7000,debug=True)

