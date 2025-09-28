import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import json # For saving/loading reminders
import os

# Create main window
root = tk.Tk()
root.title("Medication Reminder")
root.geometry("") # Lets the window size adjust to content

# Create a label
label = tk.Label(root, text="Medication Name:")
label.grid(row=0, column=0, padx=10, pady=10)

# Create an entry for medication name
med_name_entry= tk.Entry(root)
med_name_entry.grid(row=0, column=1, padx=10, pady=10)

# Create a label for dosage
dosage_label= tk.Label(root, text="Dosage (mg):")
dosage_label.grid(row=1, column=0, padx=10, pady=10)

# Create entry for dosage
dosage_entry= tk.Entry(root)
dosage_entry.grid(row=1, column=1, padx=10, pady=10)

# Create labe for time
time_label= tk.Label(root, text="Time (HH:MM, 24-hour):")
time_label.grid(row=2, column=0, padx=10, pady=10)

# Create entry for time
time_entry= tk.Entry(root)
time_entry.grid(row=2, column=1, padx=10, pady=10)

# Create a button to set reminders
def set_reminder():
    med_name = med_name_entry.get()
    dosage = dosage_entry.get()
    time = time_entry.get()
    print(f"Reminder set for {med_name}, {dosage}mg at {time}")

    if not med_name or not dosage or not time:
        messagebox.showwarning("Input Error", "Please fill all fields before setting reminder.")
        return
    try:
        datetime.strptime(time, "%H:%M")
    except ValueError:
        messagebox.showerror("Time Format Error", "Please enter time in HH:MM format (24-hour).")
        return
    save_reminder()
    reminder_listbox.insert(tk.END, f"{med_name}, {dosage}mg at {time}")
   
    # Clearing entries after setting reminder
    med_name_entry.delete(0, tk.END)
    dosage_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
set_button= tk.Button(root, text="Set Reminder", command=set_reminder)
set_button.grid(row=3, column=0, columnspan=2, pady=20)

# Optional mark taken/delete reminder
frame = tk.Frame(root)
frame.grid(row=6, column=0, columnspan=2)

def mark_taken(selection):
    if selection:
        index= selection[0]
        reminder= reminders[index]
        if not reminder.get("taken", False): # only mark once
            reminder["taken"]= True
            # Update text in the listbox
            reminder_listbox.delete(index)
            reminder_listbox.insert(index, f"{reminder['med_name']}, {reminder['dosage']}mg at {reminder['time']} (Taken)")
        else:
            messagebox.showinfo("Already Taken", "This reminder has already been marked as taken.")
    else:
        messagebox.showwarning("Selection Error", "Please select a reminder to mark as taken.")
    save_to_file()

def delete_reminder(selection):
    if selection:
        for index in reversed(selection):
            reminder_listbox.delete(index)
            del reminders[index]
            print(f"Deleted reminder at index {index}")
    else:
        messagebox.showwarning("Selection Error", "Please select a reminder to delete.")
    save_to_file()
# Buttons to mark as taken or delete
mark_taken_button= tk.Button(frame, text="Mark as Taken", command=lambda: mark_taken(reminder_listbox.curselection()))
mark_taken_button.grid(row=0, column=0, padx=10, pady=10)

delete_button= tk.Button(frame, text="Delete Reminder", command=lambda: delete_reminder(reminder_listbox.curselection()))
delete_button.grid(row=0, column=1, padx=10, pady=10)


# Internal store for reminders
reminders = []

# File to save reminders
REMINDER_FILE= "reminders.json"

def save_to_file():
    with open(REMINDER_FILE, "w") as f:
        json.dump(reminders, f, indent=4)
    print("Reminders saved to file.")

def load_from_file():
    if os.path.exists(REMINDER_FILE):
        with open(REMINDER_FILE, "r") as f:
            data= json.load(f)
            reminders.clear()
            reminders.extend(data)
            for reminder in reminders:
                text= f"{reminder['med_name']}, {reminder['dosage']}mg at {reminder['time']}"
                if reminder.get("taken", False):
                    text += " (Taken)"
                reminder_listbox.insert(tk.END, text)
        print("Reminders loaded from file.")

# Save reminders to internal list
def save_reminder():
    med_name = med_name_entry.get()
    dosage = dosage_entry.get()
    time = time_entry.get()
    if med_name and dosage and time:
        reminders.append({'med_name': med_name, 'dosage': dosage, 'time': time, 'taken': False, 'notified': False})
        messagebox.showinfo("Reminder Set", f"Reminder for {med_name}, {dosage}mg at {time} has been saved.")
        save_to_file()

# Create a listbox to show reminders
# List of reminders
reminder_label= tk.Label(root, text="Scheduled Reminders")
reminder_label.grid(row=4, column=0, columnspan=2)
reminder_listbox= tk.Listbox(root, width=50)
reminder_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Load existing reminders from file on startup
load_from_file()

# Function to check reminders
def check_reminders():
    now = datetime.now().strftime("%H:%M")
    for reminder in reminders:
        if reminder['time'] == now and not reminder.get('notified', False):
            messagebox.showinfo("Medication Reminder", f"Time to take your medication: {reminder['med_name']} ({reminder['dosage']}mg)")
            reminder['notified'] = True
    root.after(60000, check_reminders)  # Check every minute



# Run the app
check_reminders()
root.mainloop()