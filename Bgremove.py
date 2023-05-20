import cv2
import numpy as np
from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk
from colorama import init, Fore, Style

# Initialize colorama for colored output
init()

def remove_background(image_path):
    image = cv2.imread(image_path)
    
    # Apply background removal techniques (e.g., using image segmentation, chroma keying)
    # Implement your background removal algorithm here
    # For example, you can use OpenCV's grabCut algorithm
    
    mask = np.zeros(image.shape[:2], np.uint8)
    bgd_model = np.zeros((1,65),np.float64)
    fgd_model = np.zeros((1,65),np.float64)
    
    # Define the rectangle enclosing the foreground object (you can modify this based on your requirements)
    rectangle = (50, 50, image.shape[1] - 50, image.shape[0] - 50)
    
    # Apply grabCut algorithm to remove the background
    cv2.grabCut(image, mask, rectangle, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)
    
    # Create a binary mask where 0 and 2 indicate background, and 1 and 3 indicate foreground
    mask = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
    
    # Apply the mask to the image to remove the background
    removed_background_image = image * mask[:, :, np.newaxis]
    
    return removed_background_image

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((300, 300))  # Resize the image to fit the display area
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
        convert_button.config(state="normal", command=lambda: process_image(file_path))

def process_image(image_path):
    # Remove the background from the image
    removed_background_image = remove_background(image_path)

    # Save the processed image
    output_path = "./processed_image.png"
    cv2.imwrite(output_path, removed_background_image)

    # Display success message
    print(Fore.GREEN + "Image processed and saved successfully!" + Style.RESET_ALL)

# Create the main window
root = Tk()
root.title("Background Remover")

# Create a label to display the selected image
image_label = Label(root)
image_label.pack()

# Create a button to open an image file
open_button = Button(root, text="Open Image", command=open_image)
open_button.pack()

# Create a button to process the image
convert_button = Button(root, text="Process Image", state="disabled")
convert_button.pack()

# Run the main event loop
root.mainloop()
