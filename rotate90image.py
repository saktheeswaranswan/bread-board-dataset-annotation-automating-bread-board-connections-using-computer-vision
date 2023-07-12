import os
from PIL import Image

def rotate_image(image_path, output_folder):
    image = Image.open(image_path)
    image = image.rotate(45)
    image.save(os.path.join(output_folder, os.path.basename(image_path)))

if __name__ == "__main__":
    input_folder = "/home/josva/Pictures/breadboarddataset/imagecut"
    output_folder = "/home/josva/Pictures/breadboarddataset/rotated_images40it"

    for image_path in os.listdir(input_folder):
        rotate_image(os.path.join(input_folder, image_path), output_folder)

    print("Done!")
