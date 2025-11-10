# Desktop Wallpaper Quotes

A simple, user-friendly Python tool to generate beautiful wallpaper images with text quotes. Perfect for creating motivational wallpapers, presentation slides, or custom desktop backgrounds.

## Quick Start

### Option 1: Super Easy (Recommended for beginners)

**One command and you're done!**

```bash
# macOS / Linux
./run.sh

# Windows
run.bat
```

The script automatically:
- Sets up a virtual environment
- Installs all dependencies
- Generates your wallpapers
- Opens the output folder

### Option 2: Manual Setup

**Run it in 3 commands:**

```bash
# 1. Clone the repository
git clone https://github.com/pjdoland/desktop-wallpaper-quotes.git
cd desktop-wallpaper-quotes

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate wallpapers!
python desktop-wallpaper-quotes.py
```

That's it! Your wallpapers will be in the `output/` directory.

## Features

- **Zero configuration needed** - Works out of the box with sensible defaults
- **Automatic font detection** - Finds and uses system fonts automatically
- **Command-line interface** - Easy customization without editing code
- **Progress tracking** - See real-time progress as images are generated
- **Error handling** - Clear error messages if something goes wrong
- **Cross-platform** - Works on macOS, Linux, and Windows
- **Flexible customization** - Control colors, sizes, text formatting, and more

## Requirements

- Python 3.7 or higher
- Pillow (Python Imaging Library)

## Installation

### Option 1: Simple Installation (Recommended)

```bash
# Clone the repository
git clone https://github.com/pjdoland/desktop-wallpaper-quotes.git
cd desktop-wallpaper-quotes

# Install dependencies
pip install -r requirements.txt
```

### Option 2: Using Virtual Environment (Best Practice)

```bash
# Clone the repository
git clone https://github.com/pjdoland/desktop-wallpaper-quotes.git
cd desktop-wallpaper-quotes

# Create a virtual environment
python3 -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Basic Usage

Simply run the script with default settings:

```bash
python desktop-wallpaper-quotes.py
```

This will:
- Read quotes from `texts.txt` (one quote per line)
- Generate 1920x1080 wallpapers
- Use white text on black background
- Save images to the `output/` directory

### Custom Options

The script supports many command-line options for customization:

```bash
# Custom input and output
python desktop-wallpaper-quotes.py -i myquotes.txt -o wallpapers

# 4K resolution
python desktop-wallpaper-quotes.py --width 3840 --height 2160

# Different colors
python desktop-wallpaper-quotes.py --bg navy --fg white
python desktop-wallpaper-quotes.py --bg "#2C3E50" --fg "#ECF0F1"

# Larger text
python desktop-wallpaper-quotes.py --font-size 48 --text-width 40

# No text transformation (keep original case)
python desktop-wallpaper-quotes.py --text-case none
```

### All Available Options

```
Options:
  -h, --help            Show help message
  -i, --input FILE      Input text file (default: texts.txt)
  -o, --output DIR      Output directory (default: output)
  --width PIXELS        Image width (default: 1920)
  --height PIXELS       Image height (default: 1080)
  --bg, --background COLOR
                        Background color (default: black)
  --fg, --foreground COLOR
                        Text color (default: white)
  --font-size SIZE      Font size in points (default: 30)
  --text-width CHARS    Max characters per line (default: 30)
  --line-spacing PIXELS Spacing between lines (default: 15)
  --text-case CASE      Text transformation: uppercase, lowercase,
                        titlecase, or none (default: uppercase)
```

### Supported Colors

You can use named colors or hex codes:

**Named colors:** black, white, red, green, blue, yellow, cyan, magenta, gray, grey, darkgray, lightgray, navy, teal, purple, maroon, olive

**Hex codes:** `#RRGGBB` format (e.g., `#FF5733`, `#2ECC71`)

### Examples

Create motivational wallpapers:
```bash
python desktop-wallpaper-quotes.py --bg "#1a1a1a" --fg "#00ff00" --font-size 42
```

Generate phone wallpapers:
```bash
python desktop-wallpaper-quotes.py --width 1080 --height 1920 -o phone-wallpapers
```

Create presentation title slides:
```bash
python desktop-wallpaper-quotes.py --width 1920 --height 1080 --bg white --fg black --text-case titlecase
```

## Input File Format

The input file should contain one quote per line. Empty lines are ignored.

Example `texts.txt`:
```
Be the change you wish to see in the world
The only way to do great work is to love what you do
Life is what happens when you're busy making other plans
```

## Troubleshooting

### "No module named 'PIL'"
Install Pillow: `pip install Pillow`

### "Input file 'texts.txt' not found!"
Create a text file with your quotes: `echo "Your quote here" > texts.txt`

### Custom Font Not Loading
The script automatically uses system fonts. To use a custom font:
1. Place your font file (e.g., `PTMono.ttc`) in the same directory as the script
2. The script will automatically detect and use it

### Images Look Wrong
Try adjusting:
- `--font-size` - Make text bigger or smaller
- `--text-width` - Control line wrapping
- `--line-spacing` - Adjust spacing between lines

## Examples from the Repository

The repository includes Brian Eno & Peter Schmidt's "Oblique Strategies" as sample text in `texts.txt`. These are creative prompts originally designed for overcoming creative blocks.

## Advanced Usage

### Batch Processing

Generate multiple sets with different styles:

```bash
# Dark theme
python desktop-wallpaper-quotes.py -o output-dark --bg black --fg white

# Light theme
python desktop-wallpaper-quotes.py -o output-light --bg white --fg black

# Colored theme
python desktop-wallpaper-quotes.py -o output-blue --bg "#1e3a8a" --fg "#93c5fd"
```

### Integration with Other Tools

Combine with other commands:

```bash
# Generate and open the output folder
python desktop-wallpaper-quotes.py && open output

# Generate and count images
python desktop-wallpaper-quotes.py && ls -l output | wc -l

# Generate only the first 10 quotes
head -10 texts.txt > temp.txt && python desktop-wallpaper-quotes.py -i temp.txt
```

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Credits

Sample quotes are from "Oblique Strategies" by Brian Eno and Peter Schmidt.

## Support

If you encounter any issues or have questions:
1. Check the [Troubleshooting](#troubleshooting) section
2. Review the examples above
3. Open an issue on GitHub
