from flask import Flask, render_template, url_for, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    my_str = 'hello world'
    my_int = 19
    my_array = [1,2,3,4]
    my_dict = {'name': 'xiaoming',
               'age': 18
               }
    return render_template('hello.html',
                           my_str=my_str,
                           my_int=my_int,
                           my_array=my_array,
                           my_dict=my_dict
                           )


@app.route('/static')
def index2():
    print('==================')
    print('==================', url_for('static', filename='hello.js'))
    return render_template("index.html")

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method=='POST':
        result =request.form 
        return render_template("result.html", result=result)

@app.route('/set_cookies')
def set_cookie():
    resp = make_response("set_ck")
    resp.set_cookie("cookie_key", "cookie_value", max_age=60)
    return resp 

@app.route("/get_cookies")
def get_cookie():
    cookie_1 = request.cookies.get("cookie_key")
    return cookie_1 

@app.route("/delete_cookies")
def delete_cookie():
    resp = make_response("del_ck")
    resp.delete_cookie("cookie_key")
    return resp 



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

