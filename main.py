import tkinter as tk
# from .db import setup_database
from home import home_page
from booking import booking_page
from reservation import reservation_list_page
from edit_reservation import edit_reservation_page

root = tk.Tk()
root.title("Flight Reservation App")
root.geometry("700x500")

current_frame = None

def show_frame(frame_func, *args):
    global current_frame
    if current_frame:
        current_frame.destroy()
    current_frame = frame_func(root, show_frame, *args)
    current_frame.pack(fill="both", expand=True)


show_frame(home_page)
root.mainloop()
