from utils.ai_suggestions import generate_ai_suggestions

missing_skills = [
    "power bi",
    "statistics"
]

suggestions = generate_ai_suggestions(
    ["python", "sql"],
    "Data Scientist",
    missing_skills
)

print(suggestions)