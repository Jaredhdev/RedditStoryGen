from PIL import Image, ImageDraw, ImageFont


def txt_to_img(text: str, location: str) -> None:
    font = ImageFont.truetype('./fonts/Koblenz-Serial-Heavy.ttf', 70)

    left, upper, right, lower = font.getbbox(text)
    width = right - left + 10
    height = 100

    position = (5, 5)

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

