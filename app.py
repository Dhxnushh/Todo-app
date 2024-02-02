from flask import Flask,render_template,request
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
    l=[]
    for i in range(len(rows)):
        l.append(rows[i]['task'])
    print(l)
    return render_template("index.html",l=l)

if (__name__)==("__main__"):
    app.run(debug=True)