## python program -GUI-use-as-a-desktop-app

>              pip install pyinstaller


>              pyinstaller --onefile email_sender.py


### example

>             import tkinter as tk
>             from datetime import datetime, date
>             from tkcalendar import DateEntry
> 
>             # Create a new tkinter window
>              window = tk.Tk()
>              window.title("Age Calculator")
>              window.geometry("450x300")
>              window.configure(bg='#F5F5F5')
> 
>              # Create a label widget for the heading
>              heading_label = tk.Label(window, text="Age Calculator", font=("Helvetica", 18), bg="#F5F5F5")
>              heading_label.pack(pady=10)
> 
>              # Create a frame widget for the date of birth
>              dob_frame = tk.Frame(window, bg="#F5F5F5")
>              dob_frame.pack(pady=10)
>              
>              # Create a DateEntry widget for selecting the date of birth
>              dob_entry = DateEntry(dob_frame, width=12, font=("Helvetica", 12), date_pattern="dd/MM/yyyy", background='darkblue', foreground='white')
>              dob_entry.pack()
>              
>              # Create a label widget for the result
>              result_label = tk.Label(window, font=("Helvetica", 12), bg="#F5F5F5")
>              result_label.pack(pady=10)
> 
>              # Create a function to calculate age
>              def calculate_age():
>                  try:
>                      dob = dob_entry.get_date()
>                      today = date.today()
>                      age_in_days = (today - dob).days
>                      age_in_years = age_in_days // 365
>                      age_in_months = (age_in_days % 365) // 30
>                      age_in_days = (age_in_days % 365) % 30
>                      result_label.config(text=f"You are {age_in_years} years, {age_in_months} months, and {age_in_days} days old.")
>                  except ValueError:
>                      result_label.config(text="Please enter a valid date.")
> 
>              # Create a button widget to calculate age
>              calculate_button = tk.Button(window, text="Calculate Age", font=("Helvetica", 12), bg="#4CAF50", fg="#FFFFFF", command=calculate_age)
>              calculate_button.pack(pady=10)
>              
>              # Add a strip light around the outside of the window
>              strip = tk.Label(window, height=5, bg="#4CAF50")
>              strip.pack(fill=tk.X, side=tk.BOTTOM)
>              
>              # Start the tkinter event loop
>              window.mainloop()


