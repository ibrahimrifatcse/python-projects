import PySimpleGUI as sg
from datetime import datetime, date

# Create a PySimpleGUI window
sg.theme('DefaultNoMoreNagging')
layout = [[sg.Text('Enter your date of birth (DD/MM/YYYY):')],
          [sg.InputText(size=(20, 1), key='day'), sg.Text('/', pad=(0, 0)), sg.InputText(size=(20, 1), key='month'), sg.Text('/', pad=(0, 0)), sg.InputText(size=(20, 1), key='year')],
          [sg.Button('Calculate Age'), sg.Button('Exit')],
          [sg.Text(size=(50,1), key='output', font=('Helvetica', 12), text_color='#000000')]]
window = sg.Window('Age Calculator', layout)

# Create a function to calculate age
def calculate_age(dob):
    try:
        dob = datetime.strptime(dob, "%d/%m/%Y").date()
        today = date.today()
        age_in_days = (today - dob).days
        age_in_years = age_in_days // 365
        age_in_months = (age_in_days % 365) // 30
        age_in_days = (age_in_days % 365) % 30
        return f"You are {age_in_years} years, {age_in_months} months, and {age_in_days} days old."
    except ValueError:
        return "Please enter a valid date."

# Create a PySimpleGUI event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Calculate Age':
        dob = f"{values['day']}/{values['month']}/{values['year']}"
        age = calculate_age(dob)
        window['output'].update(age)

# Close the PySimpleGUI window
window.close()
