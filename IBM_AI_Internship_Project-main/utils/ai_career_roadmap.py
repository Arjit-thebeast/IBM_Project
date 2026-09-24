from utils.gemini_helper import get_gemini_response


def generate_ai_career_roadmap(
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

    Create a 6-month roadmap to become a successful {target_role}.

    Include:
    - Skills to learn
    - Projects to build
    - Interview preparation
    - Internship/job preparation

    Keep it practical and concise.
    """

    return get_gemini_response(prompt)