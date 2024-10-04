# PACKAGES
from flask import Flask, render_template, request, url_for, jsonify
from flask_assets import Environment, Bundle
import mysql.connector
import hashlib
import time



# Database
def connectDB():
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        database='adet'
    )

    return db



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

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form.get('Email')
        password = request.form.get('Password')
        password = hashlib.sha256(password.encode()).hexdigest()

        try:
            conn = connectDB()
            cursor = conn.cursor()

            query = "SELECT Email, Password FROM adet_user WHERE Email = %s AND Password = %s"
            values = (email, password)

            cursor.execute(query, values)
            user = cursor.fetchone()

            if user:
                query = "SELECT Status FROM adet_user WHERE Email = %s AND Password = %s"
                values = (email, password)

                cursor.execute(query, values)
                status = cursor.fetchone()[0]

                if status in ['Banned', 'Deleted']:
                    return render_template('userstatus.html')
                else:
                    message = "Login Successful"
                    color = '#70fa70'
                    time.sleep(1)
                    return render_template('userdashboard.html')
            else:
                raise Exception()
        except(Exception):
            message = "Login Failed, Check Details!"
            color = '#a81b1b'
        finally:
            cursor.close()
            conn.close()

        return render_template('login.html', message=message, color=color)

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html')
    elif request.method == 'POST':
        email = request.form.get('Email')
        password = request.form.get('Password')
        password = hashlib.sha256(password.encode()).hexdigest()
        fName = request.form.get('FirstName')
        lName = request.form.get('LastName')
        contactNum = request.form.get('ContactNum')
        address = request.form.get('Address')

        try:
            conn = connectDB()
            cursor = conn.cursor()

            query = "INSERT INTO adet_user (Email, HASHEDPassword, FirstName, LastName, ContactNum, Address) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (email, password, fName, lName, contactNum, address)

            cursor.execute(query, values)
            conn.commit()

            message = "User registered successfully!"
            color = '#70fa70'
        except(Exception):
            message = "Error: Failed to Register User!"
            color = '#a81b1b'
        finally:
            cursor.close()
            conn.close()
        
        return render_template('registration.html', message=message, color=color)
