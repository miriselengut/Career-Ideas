from db import create_table, load_db
from scrap import scrape, get_data, return_data
import sqlite3
import streamlit as st

def main():
    # lines = scrape("https://www.bls.gov/emp/tables/top-skills-by-detailed-occupation.htm")
    # data = get_data(lines)
    # create_table()
    # load_db(data)
    # results = query_pipeline("No formal educational credential", 49500, "Adaptability", "Computers and information technology", "Creativity and innovation")
    # print (results)
    results = return_data
    print(results[1:4])
    # results = query_average_education_by_salary(49500)
    # print(results)

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
                FROM job_list 
                WHERE edu_rank <= ?
                AND salary >= ?
                AND (
                    (skill_one = ? OR skill_two = ? OR skill_three = ?) +
                    (skill_one = ? OR skill_two = ? OR skill_three = ?) +
                    (skill_one = ? OR skill_two = ? OR skill_three = ?)
                    ) >= 2
                LIMIT 1000 OFFSET 1
                    """,
                (edu_level[current_education], str(goal_salary), skill_one, skill_one, skill_one, skill_two, skill_two, skill_two, skill_three, skill_three, skill_three))
        rows = cur.fetchall()
        columns = []
        for col in cur.description:
            columns.append(col[0])

        data = []
        for row in rows:
            row_dict = dict(zip(columns, row))
            data.append(row_dict)
    return data[:10]

def query_average_education_by_salary(goal_salary):
    conn = sqlite3.connect("/workspaces/Career-Ideas/job_list.db")
    cur = conn.cursor()
    with conn:
        cur.execute("""
                    SELECT education_needed
                    FROM job_list 
                    WHERE salary BETWEEN ? - 2000 AND ? + 2000
                    GROUP BY education_needed
                    """, 
                    (goal_salary, goal_salary))
    conn.commit()
    results = dict(cur.fetchall())
    return results

def query_average_skill_with_education(education):
    conn = sqlite3.connect("/workspaces/Career-Ideas/job_list.db")
    cur = conn.cursor()
    with conn:
        conn.execute("""
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
    
#region code without query
def pipeline(data, _education, _salary, _skill_one, _skill_two, _skill_three):
    edu_data = education(data, _education)
    salary_data = salary(edu_data, _salary)
    results = skills(salary_data, _skill_one, _skill_two, _skill_three)
    return results[:10]

def education(data, current_education):
    new_data = []
    edu_rank = edu_level[current_education]
    for item in data:
        edu_needed = item["education_needed"]
        if edu_needed not in edu_level:
            continue
        if edu_rank >= edu_level[edu_needed]:
            new_data.append(item)
    return new_data 

def salary(data, salary):
    new_data = []
    for item in data:
        if item["salary"] == "—":
            continue
        job_salary = float("".join(filter(str.isdigit, item["salary"])))
        if float(job_salary) >= salary:
            new_data.append(item)
    return new_data

def skills(data, skill_one, skill_two, skill_three):
    new_data = []
    skills = {skill_one, skill_two, skill_three}
    for item in data:
        if (
            item["skill_one"] in skills or
            item["skill_two"] in skills or
            item["skill_three"] in skills
        ):
            new_data.append(item)
    return new_data

def average_education_with_salary(data, salary):
    edu_level = {
    "No formal educational credential": 0,
    "High school diploma or equivalent": 0,
    "Some college, no degree": 0,
    "Postsecondary nondegree award": 0,
    "Associate's degree": 0,
    "Bachelor's degree": 0,
    "Master's degree": 0,
    "Doctoral or professional degree": 0
}
    for item in data:
        salary_value = int(item["salary"].strip())
        if (abs(item["salary"] - salary_value)) <= 2000:
            edu_level[item["education"]] += 1
    return edu_level

def average_skills_with_education(data, education):
    all_skills = {"Adaptability": 0,
          "Computers and information technology": 0,
          "Creativity and innovation": 0,
          "Critical and analytical thinking": 0,
          "Customer service": 0,
          "Detail oriented" : 0,
          "Fine motor": 0,
          "Interpersonal": 0,
          "Leadership": 0,
          "Mathematics": 0,
          "Mechanical": 0,
          "Physical strength and stamina": 0,
          "Problem solving and decision making": 0,
          "Project management": 0,
          "Science": 0,
          "Speaking and listening": 0,
          "Writing and reading": 0
    }
    for item in data:
        if item["education_needed"] == education:
            all_skills[item["skill_one"]] += 3
            all_skills[item["skill_two"]] += 2
            all_skills[item["skill_three"]] += 1
    return all_skills

#endregion


if __name__ == "__main__":
    main()
