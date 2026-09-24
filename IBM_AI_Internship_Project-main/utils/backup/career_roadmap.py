def generate_roadmap(target_role, missing_skills):

    roadmap = []

    roadmap.append(
        f"Target Role: {target_role}"
    )

    roadmap.append(
        "Step 1: Strengthen your existing skills"
    )

    for skill in missing_skills:
        roadmap.append(
            f"Step 2: Learn {skill.title()}"
        )

    roadmap.append(
        "Step 3: Build 2-3 projects"
    )

    roadmap.append(
        "Step 4: Complete relevant certifications"
    )

    roadmap.append(
        "Step 5: Apply for internships/jobs"
    )

    return roadmap