from flask import Flask, render_template, request
from flask_assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)

# create bundle for Flask-Assets to compile and prefix scss to css
css = Bundle('src/sass/main.sass',
             filters=['libsass'],
             output='dist/css/styles.css',
             depends='src/sass/*.sass')

assets.register("asset_css", css)
css.build()

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/credentials')
def creds():
    return render_template("credentials.html")