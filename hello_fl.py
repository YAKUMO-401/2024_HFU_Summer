from flask import Flask
from flask import abort, redirect, url_for,render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<string:username>")
def say_hello_world(username=""):
    return render_template("hi.html",name=username)

@app.route("/Apple_who")
def Apple_who():
    return "<h1>Hi! This is Apple!</h1>"

@app.route('/eat/<string:what_fruit>')
def eat_fruit(what_fruit):
    return redirect(url_for('say_fruit',fruit=what_fruit))

@app.route("/<string:fruit>")
def say_fruit(fruit):
    return "<h1>" +fruit+ " is gone.</h1>"


# @app.route('/login')
# def login():
#     abort(401)
#     this_is_never_executed()

if __name__ == "__main__":
    app.run(debug= True)