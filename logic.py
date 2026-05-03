from db import create_table, load_db
from scrap import scrape, get_data, return_data
import sqlite3
import streamlit as st


#region Skills Options
all_skills = ["Adaptability", 
          "Computers and information technology", 
          "Creativity and innovation", 
          "Critical and analytical thinking", 
          "Customer service",
          "Detail oriented",
          "Fine motor",
          "Interpersonal",
          "Leadership",
          "Mathematics",
          "Mechanical",
          "Physical strength and stamina",
          "Problem solving and decision making",
          "Project management",
          "Science",
          "Speaking and listening",
          "Writing and reading"
           ]
#endregion

#region Education Options
edu_level = {
    "No formal educational credential": 1,
    "High school diploma or equivalent": 2,
    "Some college, no degree": 3,
    "Postsecondary nondegree award": 4,
    "Associate's degree": 5,
    "Bachelor's degree": 6,
    "Master's degree": 7,
    "Doctoral or professional degree": 8
}
#endregion

def query_pipeline(current_education, goal_salary, skill_one, skill_two, skill_three):
    conn = sqlite3.connect("/workspaces/Career-Ideas/job_list.db")
    cur = conn.cursor()

    with conn:
        cur.execute("""
                SELECT *
                    FROM (
                    SELECT *, 
                    (
                    (skill_one IN (?, ?, ?)) +
                    (skill_two IN (?, ?, ?)) +
                    (skill_three IN (?, ?, ?))
                    ) AS match_score
                FROM job_list 
                WHERE edu_rank <= ?
                AND salary >= ?
        ) AS filtered_jobs
                WHERE match_score >= 2
                ORDER BY match_score DESC, salary DESC
                LIMIT 1000 OFFSET 1;
                    """,
                (
                    skill_one, skill_two, skill_three, 
                    skill_one, skill_two, skill_three, 
                    skill_one, skill_two, skill_three, 
                    edu_level[current_education], goal_salary
                ))
        
        rows = cur.fetchall()

        columns = []
        for col in cur.description:
            columns.append(col[0])

        data = []
        for row in rows:
            row_dict = dict(zip(columns, row))
            data.append(row_dict)

    return data[:10]


def query_average_skill_with_education(education):
    conn = sqlite3.connect("/workspaces/Career-Ideas/job_list.db")
    cur = conn.cursor()
    with conn:
        cur.execute("""
                    SELECT skill_one AS skill, 3 AS weight
                    FROM job_list
                    WHERE education_needed = ?

                    UNION ALL

                    SELECT skill_two AS skill, 2 AS weight
                    FROM job_list
                    WHERE education_needed = ?

                    UNION ALL

                    SELECT skill_three AS SKILL, 1 AS weight
                    FROM job_list
                    WHERE education_needed = ?
                """, (education, education, education))
        
        rows = cur.fetchall()
        results = {}
        for skill, weight in rows:
            if skill:
                results[skill] = results.get(skill, 0) + weight
        return results
