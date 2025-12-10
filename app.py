try:
    from flask import Flask, render_template, request, redirect, url_for, session, flash
    import sqlite3
    import random
    import os
    from datetime import datetime

    app = Flask(__name__)
    app.secret_key = os.urandom(24)
except ImportError:
    print("ERROR: Required packages are not installed.")
    print("Please run: pip install -r requirements.txt")
    exit(1)

# Database setup
def init_db():
    conn = sqlite3.connect('dice_rolls.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS rolls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            dice_type INTEGER,
            result INTEGER,
            timestamp DATETIME
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize database
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('dice_rolls.db')
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            flash('Registration successful! Please login.')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists. Please choose another one.')
        finally:
            conn.close()
            
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('dice_rolls.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = c.fetchone()
        conn.close()
        
        if user:
            session['logged_in'] = True
            session['username'] = username
            flash('You are now logged in')
            return redirect(url_for('dice_roller'))
        else:
            flash('Invalid credentials')
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out')
    return redirect(url_for('index'))

@app.route('/dice_roller', methods=['GET', 'POST'])
def dice_roller():
    if not session.get('logged_in'):
        flash('Please login first')
        return redirect(url_for('login'))
        
    result = None
    dice_type = None
    
    if request.method == 'POST':
        dice_type = int(request.form['dice_type'])
        result = random.randint(1, dice_type)
        
        conn = sqlite3.connect('dice_rolls.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO rolls (username, dice_type, result, timestamp) VALUES (?, ?, ?, ?)",
            (session['username'], dice_type, result, datetime.now())
        )
        conn.commit()
        conn.close()
        
    return render_template('dice_roller.html', result=result, dice_type=dice_type)

@app.route('/history')
def history():
    if not session.get('logged_in'):
        flash('Please login first')
        return redirect(url_for('login'))
        
    conn = sqlite3.connect('dice_rolls.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute(
        "SELECT * FROM rolls WHERE username = ? ORDER BY timestamp DESC LIMIT 10", 
        (session['username'],)
    )
    rolls = c.fetchall()
    conn.close()
    
    return render_template('history.html', rolls=rolls)

if __name__ == '__main__':
    app.run(debug=True)
