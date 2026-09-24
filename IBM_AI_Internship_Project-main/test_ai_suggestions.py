from utils.ai_suggestions import generate_ai_suggestions

response = generate_ai_suggestions(
    skills=["Python", "Machine Learning"],
    target_role="Data Scientist",
    missing_skills=["SQL", "Power BI"]
)

print(response)