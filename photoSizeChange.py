import cv2
import numpy as np

def convert_to_circle(image_path, sharpen=False):
    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    # Create a transparent circular mask with the same dimensions as the image
    mask = np.zeros((height, width), dtype=np.uint8)
    center = (width // 2, height // 2)
    radius = min(center[0], center[1])
    cv2.circle(mask, center, radius, (255, 255, 255), -1)

    # Create an alpha channel from the mask
    alpha = np.zeros((height, width), dtype=np.uint8)
    alpha[mask == 255] = 255

    # Merge the image and alpha channel to create a transparent circular image
    transparent_image = cv2.merge((image, alpha))

    # Apply sharpening to the circular part of the image if sharpen is True
    if sharpen:
        sharpened_image = cv2.filter2D(transparent_image, -1, np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]))
    else:
        sharpened_image = transparent_image

    return sharpened_image

# Specify the image file name and path
image_path = "./rifat.png"

# Ask the user if they want to apply sharpening
apply_sharpening = input("Apply sharpening? (y/n): ").lower() == 'y'

# Convert the image to a circular profile photo and sharpen it if specified
sharpened_image = convert_to_circle(image_path, sharpen=apply_sharpening)

# Define the desired size for the circular image
circular_size = min(sharpened_image.shape[0], sharpened_image.shape[1])

# Crop the circular image to a circular shape
center_y = sharpened_image.shape[0] // 2
center_x = sharpened_image.shape[1] // 2
radius = circular_size // 2
cropped_image = sharpened_image[center_y - radius: center_y + radius, center_x - radius: center_x + radius]

# Save the circular and (optionally) sharpened image with transparency as a PNG file
output_path = "./rifat_circular_sharpened.png"
cv2.imwrite(output_path, cropped_image)

# Display success message
print("Image converted to a circular profile photo, sharpened (if specified), and saved successfully!")
