import sqlite3

conn = sqlite3.connect("jobs.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_name TEXT NOT NULL,
    salary TEXT NOT NULL,
    job_satisfaction TEXT NOT NULL,
    dish_type TEXT NOT NULL
)
""")