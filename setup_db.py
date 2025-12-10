"""
Database setup and test script for the Dice Roller application.
Run this script to initialize the database and test connectivity.
"""

import sqlite3
import os

def init_db():
    """Initialize the database with required tables."""
    print("Initializing database...")
    
    # Create database file if it doesn't exist
    conn = sqlite3.connect('dice_rolls.db')
    c = conn.cursor()
    
    # Create tables
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
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    
    print("Database initialized successfully!")

def test_connection():
    """Test database connectivity by inserting and retrieving test data."""
    print("Testing database connection...")
    
    try:
        # Connect to database
        conn = sqlite3.connect('dice_rolls.db')
        c = conn.cursor()
        
        # Create a test user if not exists
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                     ("test_user", "test_password"))
            conn.commit()
            print("Created test user 'test_user' with password 'test_password'")
        except sqlite3.IntegrityError:
            print("Test user already exists")
        
        # Count users
        c.execute("SELECT COUNT(*) FROM users")
        user_count = c.fetchone()[0]
        print(f"Total users in database: {user_count}")
        
        # Count rolls
        c.execute("SELECT COUNT(*) FROM rolls")
        roll_count = c.fetchone()[0]
        print(f"Total dice rolls in database: {roll_count}")
        
        # Close connection
        conn.close()
        
        print("Database connection test successful!")
        return True
    
    except Exception as e:
        print(f"Error testing database connection: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("Dice Roller - Database Setup and Test")
    print("=" * 50)
    
    # Initialize database
    init_db()
    
    # Test connection
    test_connection()
    
    print("\nIf you see no errors above, the database is ready to use!")
    print("You can now run the main application with: python app.py")
    print("=" * 50)
    
    input("Press Enter to exit...")
