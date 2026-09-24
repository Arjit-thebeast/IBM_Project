from utils.gemini_helper import get_gemini_response


def generate_ai_interview_questions(
    skills,
    target_role
):

    prompt = f"""
    Skills:
    {skills}

    Target Role:
    {target_role}

    Generate 10 interview questions suitable for this role.

    Include:
    - Beginner questions
    - Intermediate questions
    - Practical questions

    Keep questions concise.
    Only output the questions.
    """

    return get_gemini_response(prompt)