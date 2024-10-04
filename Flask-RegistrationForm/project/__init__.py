# PACKAGES
from flask import Flask, render_template, request, url_for, jsonify, session, redirect
from flask_assets import Environment, Bundle
import mysql.connector
import hashlib
import time
import secrets



app = Flask(__name__)
assets = Environment(app)

# Create Bundle for Flask-Assets to compile and prefix SCSS/SASS to CSS
css = Bundle('src/sass/main.sass',
             filters=['libsass'],
             output='dist/css/styles.css',
             depends='src/sass/*.sass')

assets.register("asset_css", css)
css.build()

# Secret Key
app.secret_key = secrets.token_urlsafe(16)

# Database
def connectDB():
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        database='adet'
    )

    return db

# URL Routes:
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form.get('Email')
        password = request.form.get('Password')
        password = hashlib.sha256(password.encode()).hexdigest()

        db = connectDB()
        cur = db.cursor()
        cur.execute("SELECT UserID, Email, HASHEDPassword, Status FROM adet_user WHERE Email = %s AND HASHEDPassword = %s LIMIT 1", (email, password))
        user = cur.fetchone()
        
        if user:
            if user[3] in ['Banned', 'Deleted']:
                message = "Account is Deleted or Banned"
            else:
                message = "Login Successful!"
                session['UserID'] = user[0]
                session['Email'] = user[1]
                time.sleep(1)
                return redirect(url_for('dashboard'))
        else:
            message = "Login Failed, Check Details!"

        return render_template('login.html', message=message)

@app.route('/dashboard')
def dashboard():
    # if 'UserID' not in session:
    #     return redirect(url_for('login'))
    
    return render_template("dashboard.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

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
