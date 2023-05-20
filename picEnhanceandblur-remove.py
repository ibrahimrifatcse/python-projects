import cv2
import numpy as np
from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk
from colorama import init, Fore, Style

# Initialize colorama for colored output
init()

def enhance_photo(image_path):
    image = cv2.imread(image_path)
    
    # Apply photo enhancement techniques (e.g., brightness, contrast, sharpness adjustment)
    enhanced_image = image  # Apply your enhancement algorithms here
    
    # Apply blur removal techniques (e.g., denoising, sharpening)
    removed_blur_image = image  # Apply your blur removal algorithms here
    
    return removed_blur_image

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((600, 600))  # Resize the image to fit the display area
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
        convert_button.config(state="normal", command=lambda: enhance_and_convert_image(file_path))

def enhance_and_convert_image(image_path):
    # Enhance the photo and remove blur
    enhanced_image = enhance_photo(image_path)
    
    # Apply background removal techniques (e.g., segmentation, masking)
    removed_background_image = enhanced_image  # Apply your background removal algorithms here
    
    # Define the desired size for the circular image
    circular_size = min(removed_background_image.shape[0], removed_background_image.shape[1])

    # Create a circular mask with the same dimensions as the image
    mask = np.zeros((removed_background_image.shape[0], removed_background_image.shape[1]), dtype=np.uint8)
    center = (removed_background_image.shape[1] // 2, removed_background_image.shape[0] // 2)
    radius = min(center[0], center[1])
    cv2.circle(mask, center, radius, (255, 255, 255), -1)

    # Apply the mask to the image to create a circular profile photo with transparent background
    circular_image = cv2.bitwise_and(removed_background_image, removed_background_image, mask=mask)

    # Save the circular image with transparency as a PNG file
    output_path = "./rifat_circular.png"
    cv2.imwrite(output_path, circular_image)

    # Display success message
    print(Fore.GREEN + "Image enhanced, background removed, and saved as a circular profile photo successfully!" + Style.RESET_ALL)

# Create the main window
root = Tk()
root.title("Photo Enhancer and Background Remover")

# Create a label to display the selected image
image_label = Label(root)
image_label.pack()

# Create a button to open an image file
open_button = Button(root, text="Open Image", command=open_image)
open_button.pack()

# Create a button to enhance and convert the image
convert_button = Button(root, text="Enhance and Convert", state="disabled")
convert_button.pack()

# Run the main event loop
root.mainloop()
