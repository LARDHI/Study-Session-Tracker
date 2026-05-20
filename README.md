## Study Session Tracker

A CLI-based study session tracking application built with Python.

This project was created as a 1-Day Programming Challenge to practice building complete small-scale programs using core Python fundamentals.

📅 Challenge Information

Challenge Date: May 20, 2026
Challenge Type: One-Day Project Challenge
Status: Completed Successfully ✅

🎯 Project Goal

The goal of this project was to improve practical programming skills by building a small interactive system capable of:

tracking study sessions
storing study data
calculating statistics
organizing structured information
handling persistent data using files

The project focuses on strengthening programming fundamentals without relying on external libraries or advanced frameworks.

🧠 Concepts Practiced

This project heavily uses:

Functions
Lists
Dictionaries
Loops
Conditional Statements
File Handling
Exception Handling
Data Aggregation
Basic Statistics
State Management
CLI Program Flow
⚙️ Features
✅ Add Study Session

The user can enter:

Subject Name
Study Duration (minutes)

Each session is stored using dictionaries inside a list.

✅ View Sessions

Displays all recorded study sessions in a formatted structure.

Example:

Python        | 90 mins
Math          | 45 mins
AI            | 120 mins
✅ Save To File

Saves all study sessions into a text file.

✅ Load From File

Loads saved sessions back into the program.

✅ Study Statistics

Calculates:

Total Study Time
Average Session Duration
Longest Session
Most Studied Subject
✅ Daily Summary

Shows a summary of the total study activity for the current sessions.

✅ Input Validation

Handles invalid numeric input safely using exception handling.

📂 Project Structure
study_tracker/
│
├── main.py
├── sessions.txt
└── README.md
🗂️ Data Structure

Each study session is stored as a dictionary:

{
    "subject": "Python",
    "duration": 90,
    "date": "2026-05-20"
}

All sessions are stored inside a list during runtime.

🚀 What This Project Helped Practice

This project was designed to strengthen:

data tracking
cumulative calculations
statistics processing
structured program flow
persistent file-based storage

It also helped transition from solving isolated exercises into building complete interactive CLI applications.

📌 Notes

This project intentionally avoids:

databases
GUI frameworks
external libraries
advanced architecture patterns

to focus completely on mastering Python fundamentals first.

🔮 Possible Future Improvements

Potential upgrades include:

Session Search
Sorting System
Daily Goal Tracking
Category-Based Analytics
CSV Export
Multi-file Refactoring
🏁 Final Result

The challenge was successfully completed within one day and achieved its main goal:

building a functional study tracking system using core Python programming fundamentals.
