def recommend_skills(missing_skills):

    recommendations = []

    for skill in missing_skills:

        if skill == "machine learning":
            recommendations.append("Take Machine Learning course")

        elif skill == "sql":
            recommendations.append("Learn SQL databases")

        elif skill == "statistics":
            recommendations.append("Study Statistics for Data Science")

        elif skill == "tensorflow":
            recommendations.append("Practice Deep Learning with TensorFlow")

        elif skill == "pandas":
            recommendations.append("Learn Data Analysis using Pandas")

        else:
            recommendations.append(f"Learn {skill}")

    return recommendations