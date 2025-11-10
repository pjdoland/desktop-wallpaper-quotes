#!/usr/bin/env bash
# Simple setup and run script for Desktop Wallpaper Quotes

set -e  # Exit on error

echo "==================================="
echo "Desktop Wallpaper Quotes Generator"
echo "==================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed!"
    echo "Please install Python 3 from https://www.python.org/downloads/"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Setting up virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created!"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Check if Pillow is installed
if ! python -c "import PIL" 2>/dev/null; then
    echo "Installing dependencies..."
    pip install -q -r requirements.txt
    echo "Dependencies installed!"
fi

# Check if texts.txt exists
if [ ! -f "texts.txt" ]; then
    echo ""
    echo "Warning: texts.txt not found!"
    echo "Creating a sample texts.txt file..."
    cat > texts.txt << 'EOF'
Hello World
Welcome to Desktop Wallpaper Quotes
Create beautiful wallpapers with ease
Customize colors, fonts, and sizes
Your imagination is the only limit
EOF
    echo "Sample texts.txt created!"
fi

echo ""
echo "Running wallpaper generator..."
echo ""

# Run the script with any provided arguments
python desktop-wallpaper-quotes.py "$@"

# Show results
if [ $? -eq 0 ]; then
    echo ""
    echo "Done! Check the 'output' directory for your wallpapers."

    # Try to open the output directory
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        open output 2>/dev/null || true
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        xdg-open output 2>/dev/null || true
    fi
fi
