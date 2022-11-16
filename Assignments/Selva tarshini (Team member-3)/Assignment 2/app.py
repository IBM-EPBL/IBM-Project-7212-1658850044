from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/aboutus')
def login(): 
    return render_template('aboutus.html')

@app.route("/signin")
def blog():
    return render_template('signin.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


app.run()