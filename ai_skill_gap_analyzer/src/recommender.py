def recommend_skills(missing_skills):

    recommendations = []

    for skill in missing_skills:
        recommendations.append(f"Learn {skill} using online platforms like Coursera, Udemy, or YouTube.")

    if len(recommendations) == 0:
        recommendations.append("You already meet the skill requirements for this role.")

    return recommendations