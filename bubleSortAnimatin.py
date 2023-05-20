import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the length of the array and generate a random array of that length
arr_len = 100
arr = [random.randint(0, 100) for _ in range(arr_len)]

# Define the figure and axes for the bar plot
fig, ax = plt.subplots()
bar_rects = ax.bar(range(len(arr)), arr, align="edge")

# Define the function to update the bar plot with each animation frame
def update(frame_num):
    # Perform one step of the bubble sort algorithm
    for i in range(len(arr) - frame_num - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    
    # Update the heights of the bar rectangles with the new values in arr
    for rect, val in zip(bar_rects, arr):
        rect.set_height(val)
    
    # Return the updated bar rectangles
    return bar_rects

# Define the animation object
bubble_anim = animation.FuncAnimation(fig, update, frames=arr_len-1, repeat=True)

# Show the animation
plt.show()
