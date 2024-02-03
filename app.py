from flask import Flask,render_template,request,redirect
from cs50 import SQL
app = Flask(__name__)
db = SQL('sqlite:///user.db')
app.config['SECRET_KEY'] = 'TODO_APP'


@app.route("/",methods = ["POST","GET"])
def todo():
    if request.method=="POST":
        task = request.form.get('task')
        db.execute('insert into todo(task) values(?)',task)
    rows = db.execute('select * from todo')
    rows2 = db.execute('select * from ftodo')
    l=[]
    f=[]
    for i in range(len(rows)):
        l.append(rows[i]['task'])
    print(l)
    for i in range(len(rows2)):
        f.append(rows2[i]['task'])
    return render_template("index.html",l=l,f=f)

@app.route("/del",methods = ["POST","GET"])
def delete():
    if request.method=="POST":
        dtask = request.get_json()
        db.execute('delete from todo where task=?',dtask)
        return redirect("/")
    return redirect("/")


@app.route("/done",methods=["POST","GET"])
def done():
    if request.method=="POST":
        ftask = request.get_json()
        db.execute('insert into ftodo(task) values(?)',ftask)
        db.execute('delete from todo where task=?',ftask)
        return redirect("/")
    return redirect("/")


@app.route("/fdel",methods = ["POST","GET"])
def fdelete():
    if request.method=="POST":
        dtask = request.get_json()
        db.execute('delete from ftodo where task=?',dtask)
        return redirect("/")
    return redirect("/")


if (__name__)==("__main__"):
    app.run(debug=True)