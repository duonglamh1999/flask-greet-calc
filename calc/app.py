# Put your app in here.
from flask import Flask, request
from operations import *
app = Flask(__name__)

@app.route("/add")
def add():
    a= int(request.args.get("a"))
    b= int (request.args.get("b"))
    return str(add(a,b))
@app.route("/sub")
def sub():
    a= int(request.args.get("a"))
    b= int (request.args.get("b"))
    return str(sub(a,b))
@app.route("/mult")
def mult():
    a= int(request.args.get("a"))
    b= int (request.args.get("b"))
    return str(mult(a,b))
@app.route("/div")
def sub():
    a= int(request.args.get("a"))
    b= int (request.args.get("b"))
    return str(div(a,b))