import tkinter as tk
from tkinter import messagebox
from db import add_reservation

def booking_page(root, show_frame):
    frame = tk.Frame(root)
    tk.Label(frame, text="Book a Flight", font=("Arial", 20)).pack(pady=20)

    fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
    entries = {}

    for field in fields:
        row = tk.Frame(frame)
        row.pack(pady=5)
        tk.Label(row, text=field+":", width=15, anchor="w").pack(side="left")
        entry = tk.Entry(row, width=30)
        entry.pack(side="left")
        entries[field] = entry

    def submit():
        data = [entries[f].get() for f in fields]
        if all(data):
            add_reservation(data)
            messagebox.showinfo("Success", "Reservation added!")
            show_frame(__import__('home').home_page)
        else:
            messagebox.showerror("Error", "Please fill all fields!")

    tk.Button(frame, text="Submit", command=submit).pack(pady=20)
    tk.Button(frame, text="Back to Home", command=lambda: show_frame(__import__('home').home_page)).pack()
    return frame
