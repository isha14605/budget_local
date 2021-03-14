from flask import Flask, render_template, request

app = Flask(__name__) #turns this file into an app

# global variables here
categories_list = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/categories-submitted', methods=['POST'])
def categories_submitted():
    if int(float(request.form.get("food_val"))) != 0:
        categories_list.append('Food')
    if int(float(request.form.get("newcat1_val"))) != 0:
        newcat1 = request.form.get("newcat1")
        categories_list.append(str(newcat1))
    return render_template('locations.html', cats = categories_list)