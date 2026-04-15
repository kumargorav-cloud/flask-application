from flask import Flask, render_template,request
import pandas as pd
# in this we will learn about handling forms data
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def forms():
    username = "goravkumar"
    password = "mypassword"
    if request.method == 'GET':
        return render_template('forms.html',username=username,password=password)
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username =='goravkumar' and password == 'password':
            return "signed in successfully!!"
        else:
            return "Try again"


@app.route("/file_upload", methods=['POST'])
def file_upload():
    file = request.files['file']
    if file.content_type == 'text/plain':
        file.read().decode()
    elif file.content_type =="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" or file.content_type == "application/vnd.ms-excel":
        df = pd.read_excel(file)
        return df.to_html()


if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000,debug=True)