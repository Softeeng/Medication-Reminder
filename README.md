# Medication Reminder App

A simple desktop application built with **Python** and **Tkinter** that allows you to schedule, track, and get notified about your medications.

---

## Features
- Add reminders with:
    - Medication name
    - Dosage (mg)
    - Time (HH:MM, 24-hour format)
- View all reminders in a list
- Mark reminders as **taken**
- Delete reminders
- Get popup notifications when time to take medcation
- Saves reminders in a JSON file so they persist after restarting

---

## Tech stack
- Python
- Tkinter (GUI)
- Datetime (time management)

---

## How to Run
1. Clone this repository:
```bash
git clone https://github.com/Softeeng/Medication-Reminder.git
cd Medication-Reminder
```
2. Run the program:
```bash
python reminder_app.py
```

---

## Requirements
- Python 3.8+
- Tkinter (comes pre-installed with Python)

---

## Project Structure
```text
medication-reminder/
│── reminder_app.py       # Main application
│── reminders.json    # Stores saved reminders
│── README.md         # Documentation
│── LICENSE           # License file
```

---

## License
This project is licensed under the [MIT License] - see the (LICENSE) file for details.

---

## Future Improvements
- Add recurring reminders (daily/weekly)
- Sound alerts in addition to popup notifications
- Mobile version with push notifications
