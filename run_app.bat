@echo off
echo ==================================================
echo Dice Roller Application Setup
echo ==================================================

REM Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b
)

REM Check if virtual environment exists, create if not
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment and install dependencies
echo Activating virtual environment and installing dependencies...
call venv\Scripts\activate.bat
pip install -r requirements.txt

REM Setup database
echo.
echo Database Setup
echo --------------------------------------------------
echo Do you want to initialize/test the database before running the app?
echo This is recommended for first-time setup.
echo.
set /p setupDB="Initialize database? (Y/N): "

if /i "%setupDB%"=="Y" (
    echo Running database setup...
    python setup_db.py
)

REM Run the application
echo.
echo Starting the Dice Roller application...
echo The web application will be available at: http://127.0.0.1:5000
echo --------------------------------------------------
python app.py

pause
