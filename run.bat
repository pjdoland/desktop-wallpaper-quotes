@echo off
REM Simple setup and run script for Desktop Wallpaper Quotes (Windows)

echo ===================================
echo Desktop Wallpaper Quotes Generator
echo ===================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed!
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "venv\" (
    echo Setting up virtual environment...
    python -m venv venv
    echo Virtual environment created!
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if Pillow is installed
python -c "import PIL" >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -q -r requirements.txt
    echo Dependencies installed!
)

REM Check if texts.txt exists
if not exist "texts.txt" (
    echo.
    echo Warning: texts.txt not found!
    echo Creating a sample texts.txt file...
    (
        echo Hello World
        echo Welcome to Desktop Wallpaper Quotes
        echo Create beautiful wallpapers with ease
        echo Customize colors, fonts, and sizes
        echo Your imagination is the only limit
    ) > texts.txt
    echo Sample texts.txt created!
)

echo.
echo Running wallpaper generator...
echo.

REM Run the script with any provided arguments
python desktop-wallpaper-quotes.py %*

if errorlevel 1 (
    echo.
    echo Something went wrong. Check the error message above.
    pause
    exit /b 1
)

echo.
echo Done! Check the 'output' directory for your wallpapers.
echo.

REM Try to open the output directory
if exist "output\" (
    start output
)

pause
