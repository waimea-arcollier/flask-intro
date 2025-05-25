from flask import Flask 
from flask import render_template
from random import randint
from flask import request
from flask import redirect

#create the app
app = Flask(__name__)

# --------------------------------------
# Home Page - Loading static page
@app.get("/")
def home():
    return render_template('pages/home.jinja')

# About Page - Loading static page
@app.get("/about/")
def about():
    return render_template('pages/about.jinja')

# Random Number page - Passing a value into the template
@app.get("/random/")
def random():
    randNum = randint(1,100000)
    return render_template('pages/random.jinja', number=randNum)

# Number Page - Getting number from route and passing it into template
@app.get("/number/<int:num>")
def analyseNumber(num):
    return render_template('pages/number.jinja', number =num)

# Form page - Static page with form
@app.get("/form/")
def form():
    return render_template('pages/form.jinja')

#  Handle data posted from the form
@app.post("/processForm")
def processForm():
    print(f"Form Data: ${request.form}")
    return render_template(
        "pages/formDatat.jinja",
        name = request.form["name"],
        age = request.form["age"]
    )
    

# Handle missing pages
@app.errorhandler(404)
def errorhandler():
    return render_template('pages/404.jinja')