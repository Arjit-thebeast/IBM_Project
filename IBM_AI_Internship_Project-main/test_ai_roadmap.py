from utils.ai_career_roadmap import generate_ai_career_roadmap

response = generate_ai_career_roadmap(
    ["Python", "Machine Learning", "Deep Learning", "NLP"],
    "Data Scientist",
    ["SQL"]
)

print(response)