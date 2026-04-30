from db import create_table, load_db
from scrap import scrape, get_data

def main():
    lines = scrape("https://www.bls.gov/emp/tables/top-skills-by-detailed-occupation.htm")
    data = get_data(lines)
    create_table()
    load_db(data)
    result = pipeline(data, "Some college, no degree", 44000, "Adaptability", "Detail oriented", "Interpersonal" )
    print(len(result))
    
all_skills = ["Adaptability", 
          "Computers and information technology", 
          "Creativity and innovation", 
          "Critical and analytical thinking", 
          "Customer service",
          "Detail oriented"
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
        job_salary = int("".join(filter(str.isdigit, item["salary"])))
        if int(job_salary) >= salary:
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

# def skill_two(data, skill):
#     new_data = []
#     for item in data:
#         if item["skill_two"] == skill:
#             new_data.append(item)
#     return new_data

# def skill_three(data, skill):
#     new_data = []
#     for item in data:
#         if item["skill_three"] == skill:
#             new_data.append(item)
#     return new_data

    
if __name__ == "__main__":
    main()
