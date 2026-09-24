from utils.ai_interview_generator import generate_ai_interview_questions

response = generate_ai_interview_questions(
    ["Python", "Machine Learning", "NLP", "LangChain"],
    "Data Scientist"
)

print(response)