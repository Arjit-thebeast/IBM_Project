import pandas as pd


def clean_role_name(job_role):
    """Clean and standardize job role titles from Naukri dataset."""
    clean = str(job_role).split("|")[0].split("/")[0].split("-")[0].strip()
    clean = clean.replace("Sr ", "Senior ").replace("Sr.", "Senior ")
    clean = clean.title()
    return clean


def recommend_roles(user_skills, df=None):
    """
    Recommend job roles from Naukri dataset based on extracted user skills.
    Returns list of tuples: (clean_role, match_percentage, total_job_count)
    """
    if df is None:
        df = pd.read_csv("naukri_data_science_jobs_india.csv")

    recommendations = {}
    user_skills_lower = [s.lower() for s in user_skills]

    if not user_skills_lower:
        return []

    for _, row in df.iterrows():
        job_role = str(row.get("Job_Role", ""))
        skills_text = str(row.get("Skills/Description", "")).lower()

        # Count matched skills
        matched_skills = 0
        for skill in user_skills_lower:
            if skill in skills_text:
                matched_skills += 1

        if matched_skills > 0:
            match_percentage = (matched_skills / len(user_skills_lower)) * 100
            clean_role = clean_role_name(job_role)

            if clean_role not in recommendations:
                recommendations[clean_role] = {
                    "score": match_percentage,
                    "count": 1
                }
            else:
                current_score = recommendations[clean_role]["score"]
                recommendations[clean_role]["count"] += 1
                if match_percentage > current_score:
                    recommendations[clean_role]["score"] = match_percentage

    # Sort by match percentage desc, then by total dataset job count desc
    sorted_roles = sorted(
        recommendations.items(),
        key=lambda x: (x[1]["score"], x[1]["count"]),
        reverse=True
    )

    # Return list of (role_name, score, job_count)
    result = []
    for role, data in sorted_roles[:5]:
        result.append((role, data["score"], data["count"]))

    return result