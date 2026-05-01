from logic import query_pipeline, query_average_skill_with_education
import pytest

@pytest.fixture
def sample_data():
    return {
        "job_id": 2,
        "job_name": "Chief executives",
        "matrix_code": "11-1011",
        "self_employed": 25.9,
        "openings": "22.2",
        "salary": 206420,
        "education_needed": "Bachelor's degree",
        "education_rank": 6,
        "skill_one": "Problem solving and decision making",
        "skill_two": "Leadership",
        "skill_three": "Adaptability",
        "description": "Top executives plan strategies and policies to ensure that an organization meets its goals.",
        "work_environment": "Top executives work in nearly every industry, for both small and large organizations. They often have irregular schedules, which may include working evenings and weekends. Travel is common, particularly for chief executives."
    }

def test_query_pipeline():
    results = query_pipeline("Bachelor's degree", 49500, "Adaptability", "Leadership", "Problem solving and decision making")
    assert int(results[0]["salary"]) >= 49500

def test_query_average_skill_with_education(sample_data):
    education_level = sample_data["education_needed"]
    results = query_average_skill_with_education(education_level)
    skill_level = sample_data["skill_one"]
    assert results[skill_level] >= 2