import sqlite3
conn=sqlite3.connect('flights.db')
Create_table="""
CREATE TABLE IF NOT EXISTS reservations (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
flight_number TEXT NOT NULL,
departure_date TEXT NOT NULL,
destination TEXT NOT NULL,
date TEXT NOT NULL,
seat_number TEXT NOT NULL

)
"""
cur=conn.cursor()
cur.execute(Create_table)
conn.commit()
conn.close()