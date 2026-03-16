def generate_roadmap(missing_skills):

    roadmap = []

    month = 1

    for skill in missing_skills:

        roadmap.append(f"Month {month}: Learn {skill}")

        month += 1

    return roadmap