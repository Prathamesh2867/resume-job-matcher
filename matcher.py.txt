def match_skills(resume_skills, jobs):
    matched_jobs = []

    for job in jobs:
        matched_skills = list(set(resume_skills) & set(job["skills_required"]))
        score = len(matched_skills) / len(job["skills_required"])  # simple match score

        matched_jobs.append({
            "job_title": job["title"],
            "matched_skills": matched_skills,
            "match_score": round(score, 2)
        })

    # Sort jobs by highest match score first
    matched_jobs.sort(key=lambda x: x["match_score"], reverse=True)

    return matched_jobs
