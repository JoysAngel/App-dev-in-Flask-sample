from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my Website"

@app.route('/contact')
def contact_page():
    return "Contact Page "

@app.route('/home')
def home_page():
    return "welcome to homepage"

@app.route('/gallery')
def gallery_page():
    return "Welcome to my Gallery page"

if __name__=="__main__":
    app.run()