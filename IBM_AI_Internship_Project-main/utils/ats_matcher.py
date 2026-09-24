def calculate_ats_score(user_skills, required_skills):
    """
    Calculate ATS compatibility score comparing candidate skills against target role skills.
    Returns score %, matched_skills list, and missing_skills list.
    """
    if not required_skills:
        return {
            "score": 0.0,
            "matched_skills": [],
            "missing_skills": []
        }

    # Normalize user skills for comparison
    user_skills_lower = [str(s).lower() for s in user_skills]
    
    matched_skills = []
    missing_skills = []

    for skill in required_skills:
        skill_clean = str(skill).strip()
        skill_lower = skill_clean.lower()

        # Check exact or partial match
        if any(skill_lower in us or us in skill_lower for us in user_skills_lower):
            matched_skills.append(skill_clean)
        else:
            missing_skills.append(skill_clean)

    ats_score = (len(matched_skills) / len(required_skills)) * 100.0

    return {
        "score": round(ats_score, 1),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }