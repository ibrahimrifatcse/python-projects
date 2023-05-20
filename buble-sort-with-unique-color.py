import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the length of the array and generate a random array of that length
arr_len = 10
arr = [random.randint(0, 100) for _ in range(arr_len)]

# Define the figure and axes for the bar plot
fig, ax = plt.subplots()
bar_rects = ax.bar(range(len(arr)), arr, align="edge", color='red')
selected_rect = None

# Define the function to update the bar plot with each animation frame
def update(frame_num):
    # Perform one step of the bubble sort algorithm
    for i in range(len(arr) - frame_num - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    
    # Update the heights and colors of the bar rectangles with the new values in arr
    for i, rect in enumerate(bar_rects):
        if i == len(arr) - frame_num - 1 or i == len(arr) - frame_num:
            rect.set_color('green')  # Color for the comparing elements
        elif i > len(arr) - frame_num - 1:
            rect.set_color('skyblue')  # Color for the sorted part
        else:
            rect.set_color('red')  # Color for the remaining elements
    
        rect.set_height(arr[i])
    
    # Mark the selected array with a different color
    global selected_rect
    if selected_rect is not None:
        selected_rect.set_color('purple')  # Color for the selected array
    
    # Set the currently compared elements as the selected array
    selected_rect = bar_rects[len(arr) - frame_num - 1]
    
    # Return the updated bar rectangles
    return bar_rects

# Define the animation object
bubble_anim = animation.FuncAnimation(fig, update, frames=arr_len-1, repeat=True, interval=1000)

# Show the animation
plt.show()
