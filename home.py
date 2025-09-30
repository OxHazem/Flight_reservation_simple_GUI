import tkinter as tk

def home_page(root, show_frame):
    frame = tk.Frame(root)
    tk.Label(frame, text="Welcome to Flight Reservation System", font=("Arial", 20)).pack(pady=20)
    tk.Button(frame, text="Book Flight", width=20, command=lambda: show_frame(__import__('booking').booking_page)).pack(pady=10)
    tk.Button(frame, text="View Reservations", width=20, command=lambda: show_frame(__import__('reservations').reservation_list_page)).pack(pady=10)
    return frame