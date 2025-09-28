# 💊 Medication Reminder App

A simple desktop application built with **Python** and **Tkinter** that allows you to schedule, track, and get notified about your medications. This project is part of a **healthcare IT learning roadmap**, this is project #2 which focuses on building real-world skills in software development and applications.

---

## 📌 Features
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

## 🛠 Tech Stack
- Python
- Tkinter (GUI)
- Datetime (time management)

---

## 🚀 How to Run
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

## 💻 Requirements
- Python 3.8+
- Tkinter (comes pre-installed with Python)

---

## 📂 Project Structure
```text
medication-reminder/
│── reminder_app.py       # Main application
│── reminders.json    # Stores saved reminders
│── README.md         # Documentation
│── LICENSE           # License file
│── .gitignore
```

---

## 📖 6-Month Healthcare IT Roadmap
This project is the first in a **6-month Healthcare IT project series**, covering:
| Month | Project 1 | Project 2 |
|-------|-----------|-----------|
| 1     | Patient Record Manager ✅ | Medication Reminder ✅️ |
| 2     | Appointment Booking System | Secure Login System |
| 3     | Healthcare Analytics Dashboard | Vital Signs Tracker |
| 4     | Medical Image Viewer | Data Privacy Module |
| 5     | Telehealth Prototype | Doctor-Patient Messaging Portal |
| 6     | Portfolio Showcase | - |

---

## 📜 License
This project is licensed under the [MIT License](LICENSE).

---

## ✨️ Future Improvements
- Add recurring reminders (daily/weekly)
- Sound alerts in addition to popup notifications
- Mobile version with push notifications
