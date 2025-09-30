

# ✈️ Flight Reservation System (Tkinter + SQLite)

A **desktop flight reservation system** built with **Python Tkinter** for the user interface and **SQLite** for data storage.
The application allows users to **book flights, view reservations, edit details, and delete bookings** – all from a simple, user-friendly GUI.

## 🚀 Features

* **Home Page** – Easy navigation between booking and reservation list.
* **Book Flight** – Enter passenger details (Name, Flight Number, Departure, Destination, Date, Seat Number).
* **Reservation List** – View all stored reservations in a table.
* **Edit Reservation** – Update existing reservation details with a pre-filled form.
* **Delete Reservation** – Remove a reservation from the database.
* **Persistent Storage** – Uses **SQLite database (`flights.db`)** to store flight bookings.

---

## 🛠️ Tech Stack

* **Python 3.x**
* **Tkinter** – GUI library
* **SQLite** – Lightweight database (no extra setup required)

---

## 📂 Project Structure

```
/flight_reservation_app
  ├── main.py              # Main app window & navigation
  ├── database.py          # SQLite setup & CRUD operations
  ├── home.py              # Home page (navigation menu)
  ├── booking.py           # Flight booking form
  ├── reservations.py      # Reservation list with edit/delete
  ├── edit_reservation.py  # Edit reservation form
  ├── flights.db           # SQLite database file
  ├── requirements.txt     # Required dependencies
  └── README.md            # Project documentation
```

---

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/flight_reservation_app.git
cd flight_reservation_app
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python main.py
```



## 🎯 Use Cases

* Beginner project to learn **GUI development with Tkinter**.
* Example of **CRUD operations with SQLite** in Python.
* Can be extended into a more advanced booking system.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).


