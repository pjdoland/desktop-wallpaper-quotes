# Desktop Wallpaper Quotes

A simple Python script to create images with text from a file, centering the text on a solid background. Useful for generating title cards, presentation slides, or custom wallpapers with quotes.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Features

- Generates images with text from a file
- Centers text on a solid background
- Customizable text formatting, image size, and background color
- Supports various text cases (e.g., uppercase, lowercase, title case)

## Prerequisites

- Python 3.x
- Pillow (Python Imaging Library)

## Installation

1. Clone the repository to your local machine:

``` bash
git clone https://github.com/pjdoland/desktop-wallpaper-quotes.git
cd desktop-wallpaper-quotes
```

2. Create and activate a virtual environment (recommended):

``` bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:

``` bash
pip install -r requirements.txt
```

## Usage

1. Add your texts to the `texts.txt` file, with each text on a new line.

2. Configure the script settings in the `Configuration` section of the script.

3. Run the script:

``` bash
python desktop-wallpaper-quotes.py
```

4. The generated images will be saved in the `output` directory.

## Configuration

Customize the script settings by modifying the values in the `Configuration` section:

- `texts_file`: The name of the file containing the texts (default: "texts.txt")
- `text_color`: The text color (default: "white")
- `background_color`: The background color (default: "black")
- `image_size`: The image size in pixels (default: (1920, 1080))
- `font_file`: The font file (default: "PTMono.ttc")
- `font_size`: The font size (default: 30)
- `text_case`: The text case ("uppercase", "lowercase", "titlecase") (default: "uppercase")
- `output_dir`: The output directory for the generated images (default: "output")
- `text_width`: The maximum width of the text (default: 30)
- `line_height`: The additional spacing between lines (default: 15)

## License

This project is licensed under the [MIT License](LICENSE). See the `LICENSE` file for more details.
