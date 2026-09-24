from utils.ats_matcher import calculate_ats_score

user_skills = [
    "Python",
    "Machine Learning",
    "SQL"
]

required_skills = [
    "Python",
    "Machine Learning",
    "SQL",
    "Power BI",
    "Statistics"
]

result = calculate_ats_score(
    user_skills,
    required_skills
)

print(result)