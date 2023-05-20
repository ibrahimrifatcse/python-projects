import PySimpleGUI as sg

# Define the layout of the GUI
layout = [[sg.Text('Enter a number:', size=(15, 1)), sg.InputText(key='-INPUT-')],
          [sg.Button('Submit'), sg.Button('Exit')],
          [sg.Image(key='-IMAGE-', size=(200, 200))]]

# Create the window
window = sg.Window('Error Robot', layout)

# Define the image paths
error_image_path = 'error_robot.png'
warning_image_path = 'warning_robot.png'
info_image_path = 'info_robot.png'
smiley_image_path = 'smiley.png'

# Event loop for the GUI
while True:
    event, values = window.read()

    # Handle events
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Submit':
        # Check if the input is a number
        try:
            int(values['-INPUT-'])
        except ValueError:
            # If the input is not a number, display the error robot
            window['-IMAGE-'].update(filename=error_image_path)
            sg.Popup('Error: Invalid input', title='Error', icon=error_image_path)
        else:
            # If the input is a number, display the smiley face
            window['-IMAGE-'].update(filename=smiley_image_path)
            sg.Popup('Success: Input is a number', title='Success', icon=smiley_image_path)

# Close the window
window.close()
