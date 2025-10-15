import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

# Configuration
texts_file = "texts.txt" # name of the file where texts are located
text_color = "white"
background_color = "black"
image_size = (1920, 1080)
font_file = "PTMono.ttc"
font_size = 30
text_case = "uppercase"
output_dir = "output"
text_width = 30 # maximum width of the text
line_height = 15 # additional spacing between lines

# Create output directory if it does not exist
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# Create font object
font = ImageFont.truetype(font_file, font_size)

# Read texts from file
with open(texts_file, "r") as f:
    texts = [line.strip() for line in f]

if text_case == "uppercase":
    texts = [text.upper() for text in texts]
elif text_case == "lowercase":
    texts = [text.lower() for text in texts]
elif text_case == "titlecase":
    texts = [text.title() for text in texts]

# Create images
for i, text in enumerate(texts):
    if not text.strip():
        continue
    image = Image.new("RGB", image_size, background_color)
    draw = ImageDraw.Draw(image)

    # Wrap text
    wrapped_text = textwrap.wrap(text, width=text_width)

    # Get text size
    width, height = 0, 0
    for line in wrapped_text:
        bbox = draw.textbbox((0, 0), line, font=font)
        line_width = bbox[2] - bbox[0]
        line_height = bbox[3] - bbox[1]
        width = max(width, line_width)
        height += line_height

    # Calculate x and y coordinates to center the text
    x = (image_size[0] - width) / 2
    y = (image_size[1] - height) / 2

    # Draw text on image with additional spacing
    y_text = y
    for line in wrapped_text:
        draw.text((x, y_text), line, fill=text_color, font=font)
        bbox = draw.textbbox((0, 0), line, font=font)
        line_height_px = bbox[3] - bbox[1]
        y_text += line_height_px + line_height

    # Save image
    image.save(f"{output_dir}/{i+1}.jpg", "JPEG")
