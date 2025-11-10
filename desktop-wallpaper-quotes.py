#!/usr/bin/env python3
"""
Desktop Wallpaper Quotes Generator
A simple tool to create images with text from a file, centering the text on a solid background.
"""

import os
import sys
import argparse
import textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


def get_default_font(font_size):
    """
    Try to find a suitable system font. Falls back through multiple options.
    """
    # List of common monospace fonts across different systems
    font_options = [
        # macOS
        "/System/Library/Fonts/Monaco.ttf",
        "/System/Library/Fonts/Courier.dfont",
        "/Library/Fonts/Arial.ttf",
        # Linux
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf",
        "/usr/share/fonts/truetype/ubuntu/UbuntuMono-R.ttf",
        # Windows
        "C:/Windows/Fonts/consola.ttf",
        "C:/Windows/Fonts/cour.ttf",
        "C:/Windows/Fonts/arial.ttf",
    ]

    # First try custom font if it exists
    custom_font = Path("PTMono.ttc")
    if custom_font.exists():
        try:
            return ImageFont.truetype(str(custom_font), font_size)
        except Exception:
            pass

    # Try each system font
    for font_path in font_options:
        if Path(font_path).exists():
            try:
                return ImageFont.truetype(font_path, font_size)
            except Exception:
                continue

    # Last resort: use default PIL font
    print("Warning: Using default font (custom fonts not found)")
    return ImageFont.load_default()


def parse_color(color_string):
    """
    Parse color string. Supports named colors and hex codes.
    """
    color_string = color_string.strip().lower()

    # If it starts with #, it's a hex color
    if color_string.startswith('#'):
        return color_string

    # Named colors
    named_colors = {
        'black': '#000000',
        'white': '#FFFFFF',
        'red': '#FF0000',
        'green': '#00FF00',
        'blue': '#0000FF',
        'yellow': '#FFFF00',
        'cyan': '#00FFFF',
        'magenta': '#FF00FF',
        'gray': '#808080',
        'grey': '#808080',
        'darkgray': '#404040',
        'lightgray': '#C0C0C0',
        'navy': '#000080',
        'teal': '#008080',
        'purple': '#800080',
        'maroon': '#800000',
        'olive': '#808000',
    }

    return named_colors.get(color_string, color_string)


def apply_text_case(text, case_type):
    """
    Apply text case transformation.
    """
    if case_type == "uppercase":
        return text.upper()
    elif case_type == "lowercase":
        return text.lower()
    elif case_type == "titlecase":
        return text.title()
    else:
        return text


def generate_wallpaper(text, config, output_path):
    """
    Generate a single wallpaper image with the given text.
    """
    # Create image
    image = Image.new("RGB", config['image_size'], parse_color(config['background_color']))
    draw = ImageDraw.Draw(image)

    # Apply text case
    text = apply_text_case(text, config['text_case'])

    # Wrap text
    wrapped_text = textwrap.wrap(text, width=config['text_width'])

    # Calculate text dimensions
    total_width = 0
    total_height = 0
    line_heights = []

    for line in wrapped_text:
        bbox = draw.textbbox((0, 0), line, font=config['font'])
        line_width = bbox[2] - bbox[0]
        line_height = bbox[3] - bbox[1]
        total_width = max(total_width, line_width)
        total_height += line_height
        line_heights.append(line_height)

    # Add spacing between lines (except for the last line)
    if len(wrapped_text) > 1:
        total_height += config['line_spacing'] * (len(wrapped_text) - 1)

    # Calculate starting position to center the text
    x = (config['image_size'][0] - total_width) / 2
    y = (config['image_size'][1] - total_height) / 2

    # Draw each line
    y_position = y
    for i, line in enumerate(wrapped_text):
        draw.text((x, y_position), line, fill=parse_color(config['text_color']), font=config['font'])
        y_position += line_heights[i] + config['line_spacing']

    # Save image
    image.save(output_path, "JPEG", quality=95)


def main():
    parser = argparse.ArgumentParser(
        description="Generate desktop wallpapers with quotes from a text file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                              # Use default settings
  %(prog)s -i quotes.txt -o wallpapers  # Custom input and output
  %(prog)s --width 3840 --height 2160   # 4K resolution
  %(prog)s --bg blue --fg white         # Blue background, white text
  %(prog)s --font-size 40 --text-width 40  # Larger text
        """
    )

    parser.add_argument('-i', '--input', default='texts.txt',
                        help='Input text file (default: texts.txt)')
    parser.add_argument('-o', '--output', default='output',
                        help='Output directory (default: output)')
    parser.add_argument('--width', type=int, default=1920,
                        help='Image width in pixels (default: 1920)')
    parser.add_argument('--height', type=int, default=1080,
                        help='Image height in pixels (default: 1080)')
    parser.add_argument('--bg', '--background', dest='background_color', default='black',
                        help='Background color (default: black)')
    parser.add_argument('--fg', '--foreground', dest='text_color', default='white',
                        help='Text color (default: white)')
    parser.add_argument('--font-size', type=int, default=30,
                        help='Font size (default: 30)')
    parser.add_argument('--text-width', type=int, default=30,
                        help='Maximum characters per line (default: 30)')
    parser.add_argument('--line-spacing', type=int, default=15,
                        help='Spacing between lines in pixels (default: 15)')
    parser.add_argument('--text-case', choices=['uppercase', 'lowercase', 'titlecase', 'none'],
                        default='uppercase', help='Text case transformation (default: uppercase)')

    args = parser.parse_args()

    # Validate input file
    input_file = Path(args.input)
    if not input_file.exists():
        print(f"Error: Input file '{args.input}' not found!", file=sys.stderr)
        print(f"\nPlease create a text file with one quote per line.", file=sys.stderr)
        print(f"Example: echo 'Hello World' > {args.input}", file=sys.stderr)
        sys.exit(1)

    # Create output directory
    output_dir = Path(args.output)
    try:
        output_dir.mkdir(exist_ok=True)
        print(f"Output directory: {output_dir.absolute()}")
    except Exception as e:
        print(f"Error: Could not create output directory '{args.output}': {e}", file=sys.stderr)
        sys.exit(1)

    # Load font
    try:
        font = get_default_font(args.font_size)
        print(f"Font loaded successfully (size: {args.font_size})")
    except Exception as e:
        print(f"Error: Could not load font: {e}", file=sys.stderr)
        sys.exit(1)

    # Prepare configuration
    config = {
        'image_size': (args.width, args.height),
        'background_color': args.background_color,
        'text_color': args.text_color,
        'font': font,
        'text_width': args.text_width,
        'line_spacing': args.line_spacing,
        'text_case': args.text_case,
    }

    # Read texts from file
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            texts = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error: Could not read input file: {e}", file=sys.stderr)
        sys.exit(1)

    if not texts:
        print(f"Error: No text found in '{args.input}'", file=sys.stderr)
        sys.exit(1)

    print(f"\nGenerating {len(texts)} wallpapers...")
    print(f"Resolution: {args.width}x{args.height}")
    print(f"Colors: {args.text_color} on {args.background_color}")
    print()

    # Generate images
    success_count = 0
    for i, text in enumerate(texts, start=1):
        try:
            output_path = output_dir / f"{i}.jpg"
            generate_wallpaper(text, config, output_path)
            success_count += 1

            # Progress indicator
            progress = i / len(texts) * 100
            bar_length = 40
            filled = int(bar_length * i / len(texts))
            bar = '=' * filled + '-' * (bar_length - filled)
            print(f'\r[{bar}] {i}/{len(texts)} ({progress:.1f}%)', end='', flush=True)

        except Exception as e:
            print(f"\nWarning: Failed to generate image {i}: {e}", file=sys.stderr)

    print()  # New line after progress bar
    print(f"\nSuccess! Generated {success_count}/{len(texts)} wallpapers in '{output_dir.absolute()}'")

    if success_count < len(texts):
        print(f"Warning: {len(texts) - success_count} images failed to generate")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"\nFatal error: {e}", file=sys.stderr)
        sys.exit(1)
