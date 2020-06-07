from flask import render_template, request, redirect, url_for
from todo import app

@app.route("/")
def app():

    return render_template("index.html")

    
