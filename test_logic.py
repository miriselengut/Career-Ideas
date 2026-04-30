import pytest
from logic import education, salary, skill_one, skill_three, skill_two

data= [{
                'job_name': 'General and operations managers', 
                'matrix_code': '11-1021', 
                'self_employed': '0.9', 
                'openings': '308.7', 
                'salary': '102,950', 
                'education_needed': "Bachelor's degree", 
                'skill_one': 'Problem solving and decision making', 
                'skill_two': 'Adaptability', 
                'skill_three': 'Leadership'}, 
                {'job_name': 'Legislators[2]', 
                'matrix_code': '11-1031', 
                'self_employed': '—', 
                'openings': '2.2', 
                'salary': '44,810', 
                'education_needed': "Bachelor's degree", 
                'skill_one': 'Problem solving and decision making', 
                'skill_two': 'Leadership', 
                'skill_three': 'Adaptability'},
                {'job_name': 'Chief executives', 
                  'matrix_code': '11-1011', 
                  'self_employed': '25.9', 
                  'openings': '22.2', 
                  'salary': '206,420', 
                  'education_needed': "Bachelor's degree", 
                  'skill_one': 'Problem solving and decision making', 
                  'skill_two': 'Leadership', 
                  'skill_three': 'Adaptability'}, 
                  {'job_name': 'Construction managers', 
                   'matrix_code': '11-9021', 
                   'self_employed': '35.8', 
                   'openings': '46.8', 
                   'salary': '106,980', 
                   'education_needed': "Bachelor's degree", 
                   'skill_one': 'Problem solving and decision making', 
                   'skill_two': 'Leadership', 
                   'skill_three': 'Adaptability'}]

def test_salary(data):
    result = salary(data, 50000)
    for item in result:
        assert int(item["salary"].replace(",", "")) >=50000

def test_education(data):
    result = education(data, "Bachelor's degree")
    for item in result:
        assert item["education_needed"] == "Bachelor's degree"
    
def test_skill_one(data):
    result = skill_one(data, "Leadership")
    for item in result:
        assert item["skill_one"] == "Leadership"

def test_skill_twp(data):
    result = skill_two(data, "Problem solving and decision making")
    for item in result:
        assert item["skill_two"] == "Problem solving and decision making"

def test_skill_three(data):
    result = skill_three(data, "Adaptability")
    for item in result:
        assert item["skill_three"] == "Adaptability"
