from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/contact')
def contact_page():
    return render_template("contact.html")

@app.route('/home')
def home_page():
    return "welcome to homepage"

@app.route('/gallery')
def gallery_page():
    return "Welcome to my Gallery page"

if __name__=="__main__":
    app.run()