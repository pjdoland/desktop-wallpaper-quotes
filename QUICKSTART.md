# Quick Start Guide

Get up and running in 30 seconds!

## Method 1: One-Command Setup (Easiest)

### macOS / Linux
```bash
./run.sh
```

### Windows
```cmd
run.bat
```

The script will:
- Create a virtual environment if needed
- Install dependencies automatically
- Check for texts.txt (create sample if missing)
- Generate your wallpapers
- Open the output folder

## Method 2: Manual Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run the generator
python desktop-wallpaper-quotes.py
```

## Customizing

Add your own quotes to `texts.txt` (one per line), then run:

```bash
# macOS/Linux
./run.sh

# Windows
run.bat

# Or manually
python desktop-wallpaper-quotes.py
```

## Common Customizations

### Change colors
```bash
python desktop-wallpaper-quotes.py --bg navy --fg white
```

### 4K resolution
```bash
python desktop-wallpaper-quotes.py --width 3840 --height 2160
```

### Bigger text
```bash
python desktop-wallpaper-quotes.py --font-size 48
```

### Phone wallpapers
```bash
python desktop-wallpaper-quotes.py --width 1080 --height 1920
```

## Getting Help

```bash
python desktop-wallpaper-quotes.py --help
```

See [README.md](README.md) for complete documentation.
