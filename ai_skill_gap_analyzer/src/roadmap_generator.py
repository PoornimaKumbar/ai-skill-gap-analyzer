def generate_roadmap(missing_skills):

    roadmap = []

    for i, skill in enumerate(missing_skills):
        roadmap.append(f"Month {i+1}: Focus on learning {skill}")

    if len(roadmap) == 0:
        roadmap.append("No additional skills required. You are job-ready!")

    return roadmap