# Dice Roller Application Setup and Run Script
Write-Host "=================================================="
Write-Host "Dice Roller Application Setup" -ForegroundColor Green
Write-Host "=================================================="

# Check if Python is installed
try {
    $pythonVersion = (python --version)
    Write-Host "Python detected: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "Python is not installed or not in PATH. Please install Python and try again." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit
}

# Check if virtual environment exists, create if not
if (-not (Test-Path ".\venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
}

# Activate virtual environment and install dependencies
Write-Host "Activating virtual environment and installing dependencies..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

if ($LASTEXITCODE -ne 0) {
    Write-Host "WARNING: Could not activate virtual environment due to execution policy." -ForegroundColor Yellow
    Write-Host "Using alternative method to install dependencies..." -ForegroundColor Yellow
    & .\venv\Scripts\python.exe -m pip install -r requirements.txt
} else {
    pip install -r requirements.txt
}

# Setup database
Write-Host ""
Write-Host "Database Setup" -ForegroundColor Cyan
Write-Host "--------------------------------------------------"
$setupDB = Read-Host "Initialize database? (Recommended for first-time setup) (Y/N)"

if ($setupDB -eq "Y" -or $setupDB -eq "y") {
    Write-Host "Running database setup..." -ForegroundColor Yellow
    if (Test-Path ".\venv\Scripts\python.exe") {
        & .\venv\Scripts\python.exe setup_db.py
    } else {
        python setup_db.py
    }
}

# Run the application
Write-Host ""
Write-Host "Starting the Dice Roller application..." -ForegroundColor Green
Write-Host "The web application will be available at: http://127.0.0.1:5000" -ForegroundColor Cyan
Write-Host "--------------------------------------------------"

if (Test-Path ".\venv\Scripts\python.exe") {
    & .\venv\Scripts\python.exe app.py
} else {
    python app.py
}

Read-Host "Press Enter to exit"
