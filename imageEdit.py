from PIL import Image, ImageChops, ImageOps
import os

INPUT_FOLDER = "assets/circle"
OUTPUT_FOLDER = "assets"
TARGET_SIZE = (180, 180)   # width, height
BG_COLOR = (255, 255, 255) # white background

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def crop_to_content(img):
    img = img.convert("RGB")
    bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
    diff = ImageChops.difference(img, bg)
    bbox = diff.getbbox()

    if bbox:
        return img.crop(bbox)
    return img


for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
        input_path = os.path.join(INPUT_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, filename)

        img = Image.open(input_path)

        # crop borders
        img = crop_to_content(img)

        # resize while preserving aspect ratio
        img.thumbnail(TARGET_SIZE)

        # pad to exact same size
        final_img = Image.new("RGB", TARGET_SIZE, BG_COLOR)

        x = (TARGET_SIZE[0] - img.width) // 2
        y = (TARGET_SIZE[1] - img.height) // 2

        final_img.paste(img, (x, y))
        final_img.save(output_path)

        print(f"Processed: {filename}")