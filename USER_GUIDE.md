# Dice Roller User Guide

Welcome to the Dice Roller application! This guide will help you get started with using the application.

## Getting Started

1. Run the application using one of the following methods:
   - Double-click `run_app.bat` (recommended for most Windows users)
   - Right-click `run_app.ps1` and select "Run with PowerShell" (if you're comfortable with PowerShell)
   - Manual setup using the instructions in README.md

2. Once the application is running, open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Creating an Account

1. From the home page, click "Register" in the navigation menu
2. Enter a username and password
3. Click "Register" to create your account
4. You'll be redirected to the login page

## Rolling Dice

1. After logging in, click "Roll Dice" in the navigation menu
2. Select a dice type from the dropdown menu:
   - D4 (4-sided)
   - D6 (6-sided)
   - D8 (8-sided)
   - D10 (10-sided)
   - D12 (12-sided)
   - D20 (20-sided)
   - D100 (100-sided)
3. Click "Roll Dice" to roll the selected dice
4. The result will be displayed on the screen

## Viewing Your Roll History

1. After rolling some dice, click "History" in the navigation menu
2. You'll see a table showing your recent dice rolls
3. The table includes:
   - When the roll was made
   - The type of dice rolled
   - The result of the roll

## Logging Out

Click "Logout" in the navigation menu to log out of your account.

## Troubleshooting

### The application won't start

- Make sure Python is installed and added to your PATH
- Try running the `setup_db.py` script directly to check for errors
- Check if Flask is installed correctly by running `pip list` to see installed packages

### Database errors

- If you encounter database errors, try initializing the database again:
  - Run `python setup_db.py` from the command line
  - Or select "Y" when asked to initialize the database during startup

### Can't login or register

- Make sure the database has been initialized properly
- Try creating a new account
- If you continue to have issues, delete the `dice_rolls.db` file and reinitialize the database

## Need More Help?

If you encounter any issues not covered in this guide, please report them to the project maintainer.
