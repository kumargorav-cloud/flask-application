from flask import Flask, render_template,request,make_response,redirect,url_for

app = Flask(__name__)

#simple route to check the connectivity
@app.route("/")
def index():
# sending status code by ownself
#sending total response by ownself
    #response = make_response("this is to test the flask application")
    #response.headers['content-type'] = "application/octet-stream"
    #response.status_code = 202
    #return response
    return "this is to test flaks application"


#route to extrat html file
@app.route("/htmlfile" , methods=['POST','GET'])
def htmlfile():
    # if we want to send the data to the html file
    myval1 = 'gorav'
    myval2 = 'kumar'
    mylist = ['10','23','44','55']
    if request.method == 'GET':
        return render_template('first.html', myval1=myval1,myval2=myval2,mylist=mylist)
    elif request.method == 'POST':
        return "this is post request"
    else:
        return "this is default GET request"



#giving input as a user
@app.route("/greet/<name>")
def greet(name):
    return f"Hello {name}"


@app.route("/add/<int:number1>/<int:number2>")
def add(number1,number2):
    return f"This addition is {number1+number2}"

#handle url parameters
@app.route("/handle_url_params")
def url_params():
    if 'gretting' in request.args.keys() and 'name' in request.args.keys():
        gretting = request.args['gretting']
        name = request.args.get('name')
        return f"{gretting},{name}"
    
    else:
        return "some parameters are missing!!"



@app.route("/filters")
def filters():
    some_text = "Hello Filter"
    return render_template('filters.html',some_text=some_text)

# getting the page with the help of redirect

@app.route("/redirect_endpoint")
def redirect_endpoint():
    return redirect(url_for('filters'))


if __name__ == "__main__":
    app.run(host="127.0.0.1",port=3000,debug=True)

