def find_skill_gap(user_skills, job_skills):

    user_set = set([s.strip().lower() for s in user_skills])
    job_set = set([s.strip().lower() for s in job_skills])

    missing_skills = job_set - user_set

    match_percentage = (len(user_set & job_set) / len(job_set)) * 100

    return list(missing_skills), round(match_percentage,2)