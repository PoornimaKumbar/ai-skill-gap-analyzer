def find_skill_gap(user_skills, job_skills):

    # Clean and convert to sets
    user_set = set([s.strip().lower() for s in user_skills if s.strip() != ""])
    job_set = set([s.strip().lower() for s in job_skills if s.strip() != ""])

    # Find missing skills
    missing_skills = list(job_set - user_set)

    # Prevent division by zero
    if len(job_set) == 0:
        match_percentage = 0
    else:
        match_percentage = (len(user_set & job_set) / len(job_set)) * 100

    return missing_skills, round(match_percentage, 2)