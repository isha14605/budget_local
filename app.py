from flask import Flask, render_template, request

app = Flask(__name__) #turns this file into an app

@app.route('/')
def index():
    return render_template('index.html')