from PIL import Image, ImageDraw, ImageFont
import textwrap


def create_title_img(title: str, folder: str) -> None:
    font = ImageFont.truetype('./fonts/verdanab.ttf', 20)
    wrapped_title = textwrap.wrap(title, width=55)
    num_lines = len(wrapped_title)

    width = 700
    height = 20 * num_lines + 50
    position = (30, 135)

    wrapped_title = '\n'.join(wrapped_title)
    img = Image.new('RGB', (width, height+70+120), (255, 255, 255))
    img_top = Image.open('./images/title_top.jpg')
    img_bottom = Image.open('./images/title_bottom.jpg')
    img.paste(img_top, (0, 0))
    img.paste(img_bottom, (0, height + 120))
    d = ImageDraw.Draw(img)

    d.text((position[0], position[1]), wrapped_title, font=font, fill='black')
    img.save(f"{folder}/img_title.png")


def txt_to_img(text: str, location: str) -> None:
    font = ImageFont.truetype('./fonts/Koblenz-Serial-Heavy.ttf', 120)

    left, upper, right, lower = font.getbbox(text)
    width = right - left + 50
    height = 150

    position = (20, 5)

    # Create transparent PNG
    img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    d = ImageDraw.Draw(img)

    # Add text with black outline
    outline_width = 5
    d.text((position[0] - outline_width, position[1]), text, font=font, fill="black")
    d.text((position[0] + outline_width, position[1]), text, font=font, fill="black")
    d.text((position[0], position[1] - outline_width), text, font=font, fill="black")
    d.text((position[0], position[1] + outline_width), text, font=font, fill="black")

    # Add main white text
    d.text(position, text, font=font, fill="white")
    img.save(location)


def create_images(text_array: list, folder: str) -> None:
    for i, element in enumerate(text_array):
        txt_to_img(element, f"{folder}/img_{i}.png")



