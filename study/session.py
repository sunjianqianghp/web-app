from flask import render_template 
from flask import make_response
from flask import Flask, session, redirect, url_for, request 

app = Flask(__name__)
app.secret_key = 'abcdefghijklmn'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return f"登录用户名：{username} <br><b><a href='/logout'>注销</a></b>"
    return "您暂未登录<br><a href='/login'>登录 </a>"

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method=='POST':
        session['username'] = request.form['username']
        print(session.items())
        return redirect(url_for('index'))

    else:
        return '''<form action = "" method="post">
            <p><input type="text" name="username"/></p>
            <p><input type="submit" value="登录"/></p>
                </form> 
                '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))



if __name__=='__main__':
    app.run(debug=True)


