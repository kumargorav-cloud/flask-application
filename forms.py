from flask import Flask, render_template,request,Response,send_from_directory
import pandas as pd
import uuid
# in this we will learn about handling forms data
import os
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


@app.route("/convert_to_csv",methods=['POST'])
def convert_to_csv():
    file = request.files['file']
    df = pd.read_excel(file)

    response = Response(
        df.to_csv(),
        mimetype='text/csv',
        headers={
            'Content-Disposition':'attachment; filename=result.csv'
        }
    )
    return response

@app.route("/convert_csv_two",methods=['POST'])
def convert_csv_two():
    file = request.files['file']
    df = pd.read_excel(file)

    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    filename = f"{uuid.uuid4()}.csv"
    
    df.to_csv(os.path.join('downloads',filename))
              
    return render_template('downloads.html',filename=filename)


@app.route("/download/<filename>")
def download(filename):
    return send_from_directory('downloads',filename,download_name='result.csv')


@app.route("/handle_request", methods=['POST'])
def handle_request():
    gretting = request.json['gretting']
    name = request.json['name']

    with open('file.txt','w') as f:
        f.write(f"{gretting},{name}")

    return {'message':'success'}




if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000,debug=True)