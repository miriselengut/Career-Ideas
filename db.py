import sqlite3

def create_table():
    conn = sqlite3.connect("/workspaces/Career-Ideas/job_list.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS job_list (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_name TEXT NOT NULL,
        matrix_code INT NOT NULL,
        self_employed INT NOT NULL,
        openings TEXT NOT NULL,
        salary INT NOT NULL,
        education_needed INT NOT NULL,
        skill_one TEXT NOT NULL,
        skill_two INT NOT NULL,
        skill_three INT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def load_db(data):
    conn = sqlite3.connect("/workspaces/Career-Ideas/job_list.db")
    cur = conn.cursor()

    for item in data:
        cur.execute("INSERT INTO job_list (job_name, matrix_code, self_employed, openings, salary, education_needed, skill_one, skill_two, skill_three) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (item["job_name"], item["matrix_code"], item["self_employed"], item["openings"], item["salary"], item["education_needed"], item["skill_one"], item["skill_two"], item["skill_three"]))
 
    conn.commit()
    conn.close()
