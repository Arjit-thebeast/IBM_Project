def generate_interview_questions(skills):

    questions = []

    skill_questions = {
        "python": [
            "What are Python lists and tuples?",
            "What is the difference between list and dictionary?"
        ],

        "sql": [
            "What is a JOIN in SQL?",
            "Difference between WHERE and HAVING?"
        ],

        "machine learning": [
            "What is overfitting?",
            "Difference between supervised and unsupervised learning?"
        ],

        "power bi": [
            "What are dashboards in Power BI?",
            "What is DAX?"
        ]
    }

    for skill in skills:

        skill_lower = skill.lower()

        if skill_lower in skill_questions:
            questions.extend(
                skill_questions[skill_lower]
            )

    return questions