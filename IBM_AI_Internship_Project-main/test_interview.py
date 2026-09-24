from utils.ai_interview_generator import generate_ai_interview_questions

skills = [
    "Python",
    "SQL",
    "Machine Learning"
]

questions = generate_ai_interview_questions(skills, "Data Scientist")
print(questions)