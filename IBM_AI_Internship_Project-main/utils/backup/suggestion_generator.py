def generate_suggestions(missing_skills):

    suggestions = []

    for skill in missing_skills:

        if skill == "sql":
            suggestions.append(
                "Learn SQL and practice database queries."
            )

        elif skill == "machine learning":
            suggestions.append(
                "Build ML projects using Scikit-Learn."
            )

        elif skill == "deep learning":
            suggestions.append(
                "Learn TensorFlow or PyTorch."
            )

        elif skill == "nlp":
            suggestions.append(
                "Work on NLP projects using spaCy."
            )

        else:
            suggestions.append(
                f"Improve your knowledge of {skill}."
            )

    return suggestions