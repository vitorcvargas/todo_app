from flask import render_template, request, redirect, url_for
from todo import app
from .models import *

@app.route("/")
def index():

    todos = Todo.query.all()

    return render_template("index.html", todos = todos)

#-------------------------------------------------------------#

@app.route("/add", methods = ["POST"])
def add():

    title = Todo(title = request.form.get("title"))
    db.session.add(title)

    db.session.commit()

    return redirect(url_for("index"))

@app.route("/delete/<int:id>")
def delete(id):
    item = Todo.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()

    return redirect(url_for("index"))

#-------------------------------------------------------------#

@app.route("/update/<int:id>", methods = ["GET", "POST"])
def update(id):
    if request.method == "POST":

        item = Todo.query.get_or_404(id)
        update = request.form.get("title")
        item.title = update
        db.session.commit()

        return redirect(url_for('index'))

    else:
        item = request.form.get("title")
        return render_template('update.html', item = item)

#-------------------------------------------------------------#

@app.route("/crossoff/<int:id>")
def crossoff(id):
    
    item = Todo.query.get_or_404(id)
    item.completed = True
    db.session.commit()

    return redirect(url_for('index'))
#--------------------------------------------------------------#

@app.route("/uncross/<int:id>")
def uncross(id):
    item = Todo.query.get_or_404(id)
    item.completed = False
    db.session.commit()

    return redirect(url_for('index'))


    
