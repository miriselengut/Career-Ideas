import sqlite3

def create_table():
    conn = sqlite3.connect("jobs.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_name TEXT NOT NULL,
        salary INT NOT NULL,
        job_satisfaction INT NOT NULL,
        job_meaning INT NOT NULL
    )
    """)
    
    conn.commit()
    conn.close()

def load_db(data):
    conn = sqlite3.connect("jobs.db")
    cur = conn.cursor()

    for item in data:
        cur.execute("INSERT INTO jobs (job_name, salary, job_satisfaction, job_meaning) VALUES (?, ?, ?, ?)",
                (item["job_name"], item["salary"], item["job_satisfaction"], item["job_meaning"]))

    conn.commit()
    conn.close()