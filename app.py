from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def home():
  return "<h1>Hello world!</h1>"

