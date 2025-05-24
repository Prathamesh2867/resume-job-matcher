from resume_parser import extract_skills_from_resume
from job_scraper import get_mock_job_description
from matcher import match_skills
from report_generator import generate_excel_report

def main():
    # Load resume from text file
    resume_file = "resume.txt"
    with open(resume_file, "r", encoding="utf-8") as file:
        resume_text = file.read()

    # Step 1: Extract skills from resume
    extracted_skills = extract_skills_from_resume(resume_text)
    print("Skills found in resume:", extracted_skills)

    # Step 2: Get mock job descriptions
    job_descriptions = get_mock_job_description()
    print("Job descriptions loaded.")

    # Step 3: Match resume skills with job descriptions
    matched_results = match_skills(extracted_skills, job_descriptions)
    print("Matching done.")

    # Step 4: Generate Excel report
    output_file = "matched_jobs_report.xlsx"
    generate_excel_report(matched_results, output_file)
    print(f"Excel report generated: {output_file}")

if __name__ == "__main__":
    main()
