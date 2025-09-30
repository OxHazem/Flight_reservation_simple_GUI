import tkinter as tk
from database import get_reservations, delete_reservation

def reservation_list_page(root, show_frame):
    frame = tk.Frame(root)
    tk.Label(frame, text="Reservations List", font=("Arial", 20)).pack(pady=20)
    table_frame = tk.Frame(frame)
    table_frame.pack()

    def load_data():
        for widget in table_frame.winfo_children():
            widget.destroy()
        reservations = get_reservations()
        headers = ["ID", "Name", "Flight", "Departure", "Destination", "Date", "Seat", "Actions"]
        for col, header in enumerate(headers):
            tk.Label(table_frame, text=header, borderwidth=1, relief="solid", width=12).grid(row=0, column=col)
        for row_idx, row in enumerate(reservations, start=1):
            for col_idx, val in enumerate(row):
                tk.Label(table_frame, text=val, borderwidth=1, relief="solid", width=12).grid(row=row_idx, column=col_idx)
            tk.Button(table_frame, text="Edit", command=lambda r=row: show_frame(__import__('edit_reservation').edit_reservation_page, r)).grid(row=row_idx, column=len(row))
            tk.Button(table_frame, text="Delete", command=lambda rid=row[0]: [delete_reservation(rid), load_data()]).grid(row=row_idx, column=len(row)+1)

    load_data()
    tk.Button(frame, text="Back to Home", command=lambda: show_frame(__import__('home').home_page)).pack(pady=10)
    return frame
