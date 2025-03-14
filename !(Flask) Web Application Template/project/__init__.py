from flask import Flask, render_template, request
from flask_assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)

# Create Bundle for Flask-Assets to compile and prefix SCSS/SASS to CSS
css = Bundle('src/sass/main.sass',
             filters=['libsass'],
             output='dist/css/styles.css',
             depends='src/sass/*.sass')

assets.register("asset_css", css)
css.build()

# URL Routes:
@app.route('/')
def index():
    return render_template("index.html")