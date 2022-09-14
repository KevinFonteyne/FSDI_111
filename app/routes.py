from flask import Flask, render_template     # from the flask "module" import Flask class

app = Flask(__name__)       # Instantiate a Flask class into the app variable


# @app.get("/")   #decorator that allows us to map routes to "view functions"
# def index():    # Flask calls these "view functions"
#     return "<h1>Hello, world!</h1>" # return statement

@app.get("/")
def index():
    return render_template("index.html")


@app.get("/about")
def about():
    me = {
        "first_name": "Kevin",
        "last_name": "Fonteyne",
        "hobbies": "Gaming",
        "bio": "My name is Kevin and I love jinja"
    }
    return render_template("about.html", about_dict=me)

@app.get("/objects")
def objects():
    return render_template("objects.html")   