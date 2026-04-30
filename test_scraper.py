import pytest
import os
from db import create_table, load_db
from scrap import get_data
import sqlite3

@pytest.fixture
def db():
    conn = sqlite3.connect("job_list.db")
    cursor = conn.cursor()
    yield cursor
    conn.close()

def test_database_created():
    create_table()
    assert os.path.exists("job_list.db")

def test_database_loaded(db):
    data = get_data()
    load_db(data)
    row = db.execute("SELECT * FROM job_list LIMIT 1").fetchone()
    assert row is not None 

def test_scraper():
    data = get_data()
    assert data is not None

