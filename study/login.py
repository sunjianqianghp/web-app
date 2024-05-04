from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # print(url_for("static", filename="login.html"))
    return render_template("login.html")


@app.route('/success/<name>')
def success(name):
    return f'welcomm {name}'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print('Post request')
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        print('Get')
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug=True)



