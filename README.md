# Dice Roller Web Application

A Flask-based web application that allows users to roll virtual dice and keep track of their roll history.

## Features

- User registration and login system
- Roll different types of dice (d4, d6, d8, d10, d12, d20, d100)
- Store roll history in a SQLite database
- View your roll history

## Installation

### Easy Setup (Windows)

1. Simply double-click the `run_app.bat` file to:
   - Create a virtual environment
   - Install all required dependencies
   - Start the application

### Manual Setup

1. Clone this repository or download the files
2. Create a virtual environment (recommended):
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the Flask application:
   ```
   python app.py
   ```
3. Open your web browser and navigate to `http://127.0.0.1:5000`

## Database

The application uses SQLite to store user information and roll history. The database file `dice_rolls.db` will be created automatically when you first run the application.

## Project Structure

- `app.py` - Main application file
- `templates/` - HTML templates
- `static/` - Static files (CSS, JavaScript, etc.)
- `dice_rolls.db` - SQLite database (created on first run)

## Security Notice

This is a demonstration application. In a production environment, you should:
- Use a more secure method for password storage (e.g., bcrypt)
- Configure Flask with a proper secret key
- Use HTTPS for all connections
- Implement proper input validation and CSRF protection
