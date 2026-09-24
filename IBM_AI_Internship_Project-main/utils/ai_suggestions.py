from utils.gemini_helper import get_gemini_response


def generate_ai_suggestions(
    skills,
    target_role,
    missing_skills
):

    prompt = f"""
    User Skills:
    {skills}

    Target Role:
    {target_role}

    Missing Skills:
    {missing_skills}

    Give 5 career improvement suggestions.
    Keep the answer short and practical.
    """

    return get_gemini_response(prompt)