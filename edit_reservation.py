import tkinter as tk
from tkinter import messagebox
from database import update_reservation

def edit_reservation_page(root, show_frame, reservation):
    frame = tk.Frame(root)
    tk.Label(frame, text="Edit Reservation", font=("Arial", 20)).pack(pady=20)

    fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
    entries = {}

    for i, field in enumerate(fields, start=1):
        row = tk.Frame(frame)
        row.pack(pady=5)
        tk.Label(row, text=field+":", width=15, anchor="w").pack(side="left")
        entry = tk.Entry(row, width=30)
        entry.insert(0, reservation[i])
        entry.pack(side="left")
        entries[field] = entry

    def update():
        data = [entries[f].get() for f in fields]
        if all(data):
            update_reservation(reservation[0], data)
            messagebox.showinfo("Success", "Reservation updated!")
            show_frame(__import__('reservations').reservation_list_page)
        else:
            messagebox.showerror("Error", "Please fill all fields!")

    tk.Button(frame, text="Update", command=update).pack(pady=20)
    tk.Button(frame, text="Back", command=lambda: show_frame(__import__('reservations').reservation_list_page)).pack()
    return frame
