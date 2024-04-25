import os

from PIL import Image, ImageFont, ImageDraw

CURRENT_DIRECTORY = os.getcwd()


def path_input():
    """Returns the image and output path for the image(relative)."""
    try:
        img_path = input("Enter your image's relative path: ")
        out_path = input("What should be the name of your watermark image?: ")
    except FileNotFoundError:   # For incorrect file path
        print("Please enter a valid path")
    else:
        return img_path, out_path


def watermark(image_path, output_path):
    """Watermarks the image and saves it as a png file."""
    # Convert the image to a usable format
    img = Image.open(image_path).convert('RGBA')
    image_width, image_height = img.size
    # Font size
    size = image_height / 30
    font = ImageFont.truetype("OpenSans.ttf", size=size)

    text = input("Watermarker text: ")

    # Creating the watermark surface
    watermarker_img = Image.new('RGBA', (image_width, image_height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(watermarker_img)
    color_pattern = (255, 255, 255, 30)

    # To create the pattern for the watermark's surface
    for i in range(0, image_width*2, 50):
        draw.line([(0, image_width-i), (i, image_height)], fill=color_pattern, width=5)

    # Watermark text
    _, _, text_width, text_height = draw.textbbox((0, 0), text, font=font)
    x = (image_width-text_width) // 2
    y = (image_height-text_height) // 2
    text_color_pattern = (255, 255, 255, 130)
    draw.text((x, y), text, font=font, fill=text_color_pattern)

    # Merging and saving the images
    final_image = Image.alpha_composite(img, watermarker_img)
    final_image.save(os.path.join(CURRENT_DIRECTORY, output_path + '.png'), format='PNG')


path1, path2 = path_input()
watermark(image_path=path1, output_path=path2)
