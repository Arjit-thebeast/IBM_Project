from utils.role_recommender import recommend_roles

skills = [
    "Python",
    "Machine Learning",
    "SQL"
]

recommendations = recommend_roles(skills)

for role, score, job_cnt in recommendations:
    print(f"{role} --> Match Score: {score:.0f}% ({job_cnt} jobs)")