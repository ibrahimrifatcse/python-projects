import tkinter as tk
from datetime import datetime, date

# Create a new tkinter window
window = tk.Tk()
window.title("Age Calculator")
window.geometry("450x300")
window.configure(bg='#F5F5F5')

# Create a label widget for the heading
heading_label = tk.Label(window, text="Age Calculator", font=("Helvetica", 18), bg="#F5F5F5")
heading_label.pack(pady=10)

# Create a frame widget for the date of birth
dob_frame = tk.Frame(window, bg="#F5F5F5")
dob_frame.pack(pady=10)

# Create an entry widget for the day
day_entry = tk.Entry(dob_frame, width=2, font=("Helvetica", 12))
day_entry.pack(side=tk.LEFT)

# Create a label widget for the slash separator
slash_label1 = tk.Label(dob_frame, text="/", font=("Helvetica", 12), bg="#F5F5F5")
slash_label1.pack(side=tk.LEFT)

# Create an entry widget for the month
month_entry = tk.Entry(dob_frame, width=2, font=("Helvetica", 12))
month_entry.pack(side=tk.LEFT)

# Create a label widget for the slash separator
slash_label2 = tk.Label(dob_frame, text="/", font=("Helvetica", 12), bg="#F5F5F5")
slash_label2.pack(side=tk.LEFT)

# Create an entry widget for the year
year_entry = tk.Entry(dob_frame, width=4, font=("Helvetica", 12))
year_entry.pack(side=tk.LEFT)

# Create a label widget for the result
result_label = tk.Label(window, font=("Helvetica", 12), bg="#F5F5F5")
result_label.pack(pady=10)

# Create a function to calculate age
def calculate_age():
    try:
        dob = datetime.strptime(f"{day_entry.get()}/{month_entry.get()}/{year_entry.get()}", "%d/%m/%Y").date()
        today = date.today()
        age_in_days = (today - dob).days
        age_in_years = age_in_days // 365
        age_in_months = (age_in_days % 365) // 30
        age_in_days = (age_in_days % 365) % 30
        result_label.config(text=f"You are {age_in_years} years, {age_in_months} months, and {age_in_days} days old.")
    except ValueError:
        result_label.config(text="Please enter a valid date.")

# Create a button widget to calculate age
calculate_button = tk.Button(window, text="Calculate Age", font=("Helvetica", 12), bg="#4CAF50", fg="#FFFFFF", command=calculate_age)
calculate_button.pack(pady=10)

# Add a strip light around the outside of the window
strip = tk.Label(window, height=5, bg="#4CAF50")
strip.pack(fill=tk.X, side=tk.BOTTOM)

# Start the tkinter event loop
window.mainloop()
