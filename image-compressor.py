from PIL import Image
import os

def compress_image(input_path, output_path, quality=90):
    with Image.open(input_path) as image:
        # Convert the image to JPEG format with the specified quality
        image.save(output_path, "JPEG", quality=quality)

    print("Image compression completed successfully!")


# Example usage
input_path = "./input_image.jpg"
output_path = "./compressed_image.jpg"

compress_image(input_path, output_path, quality=80)
