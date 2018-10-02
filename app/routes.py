from flask import Flask, render_template
from app import app

form =render_template("form.html")
@app.route('/')
def index():
    return form


