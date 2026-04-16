from flask import Flask,render_template,session,make_response,request,flash

app = Flask(__name__,static_folder='static',static_url_path='/')

app.secret_key = 'any key'

@app.route("/")
def simple():
    return render_template('staticfile.html',message='index file')


# creating session data
@app.route("/set_data")
def set_data():
    session['name'] = "gorav"
    session['other'] = "Hello gorav"
    return render_template('staticfile.html',message='session data set.')


@app.route("/get_data")
def get_data():
    if 'name' in session.keys() and 'other' in session.keys():
        name = session['name']
        other = session['other']
        return render_template('staticfile.html',message=f"{name}, {other}")
    else:
        return render_template('staticfile.html',message='No session found!!')

@app.route("/clear_data")
def clear_data():
    session.clear()
    # if we want to clean any specific thing
    # session.pop('name')
    return render_template("staticfile.html",message='session cleared!!')


# working with cookies , uses on client side
@app.route("/set_cookies")
def set_cookies():
    response = make_response(render_template('staticfile.html',message='set cookies'))
    response.set_cookie('name','gorav')
    return response

@app.route("/get_cookies")
def get_cookies():
    cookie_value = request.cookies['name']
    return render_template('staticfile.html',message=f"Cookie:{cookie_value}")


@app.route('/remove_cookie')
def remove_cookie():
    response = make_response(render_template('staticfile.html',message='cookie removed'))
    response.set_cookie('cookie_name',expires=0)
    return response
    
# creating form apge

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'gorav' and password == '12345':
            flash("login successfully!!")
            return render_template('staticfile.html',message='')
        else:
            flash("Login failed!!")
            return render_template('staticfile.html',message='')


if __name__ == "__main__":
    app.run(host="127.0.0.1",port=7000,debug=True)

