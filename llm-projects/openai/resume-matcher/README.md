# Resume Matcher

Project using OpenAI API

## Goal

Use reasoning-capable LLM to compare a resume to a job description and suggest changes to improve matching.

## Workflow

1. Place your resume in `resume.txt` and job description in `job_description.txt`.
2. Run the matcher script:
	```powershell
	C:/STEVE/DEV/llm-projects/.venv/Scripts/python.exe openai/resume-matcher/resume_matcher.py
	```
3. The match report will be saved to `match_report.txt`.

## Prompt
The script uses the following prompt for the LLM:

> You are an expert career advisor.
> Given the following resume and job description, analyze how closely the resume matches the job requirements.
> List key skills, experiences, and qualifications that are present in both, and highlight any gaps or missing requirements.
> Provide a match score from 0 to 100, and a brief explanation of your reasoning.

## Files
- `resume_matcher.py`: Main script for matching.
- `resume.txt`: Input resume.
- `job_description.txt`: Input job description.
- `match_report.txt`: Output report.
