import time

from flask import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/name/<name>")
def test(name=None):
    return render_template("test.html", name=name)

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            session['user'] = request.form['user']
            return 'Admin login successfully!'
        else:
            return 'No such user!'
    if 'user' in session:
        return 'Hello %s!' % session['user']
    else:
        title = request.args.get('title', 'Default')
        return render_template('login.html', title=title)
@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))

app.secret_key = "123123"

if __name__ == '__main__':
    app.run()
