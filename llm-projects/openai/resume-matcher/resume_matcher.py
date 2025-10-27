import openai
import httpx
import os

# PDF support
import pdfplumber

# Read API key from file
with open("openai/openai_api_key.txt", "r") as f:
    api_key = f.read().strip()

client = openai.OpenAI(
    api_key=api_key,
    http_client=httpx.Client(verify=False)
)

# Accept .md or .pdf for resume input
resume_md = "openai/resume-matcher/resume.md"
resume_pdf = "openai/resume-matcher/resume.pdf"
jd_path = "openai/resume-matcher/job-description.txt"
output_path = "openai/resume-matcher/match_report.txt"

if os.path.exists(resume_md):
    with open(resume_md, "r", encoding="utf-8") as f:
        resume_text = f.read()
elif os.path.exists(resume_pdf):
    with pdfplumber.open(resume_pdf) as pdf:
        resume_text = "\n".join(page.extract_text() or "" for page in pdf.pages)
else:
    print(f"Resume file not found. Please provide either '{resume_md}' or '{resume_pdf}'.")
    exit(1)

if not os.path.exists(jd_path):
    print(f"Job description file '{jd_path}' not found.")
    exit(1)

with open(jd_path, "r", encoding="utf-8") as f:
    jd_text = f.read()

prompt = (
    "You are an expert career advisor.\n"
    "Given the following resume and job description, analyze how closely the resume matches the job requirements.\n"
    "List key skills, experiences, and qualifications that are present in both, and highlight any gaps or missing requirements.\n"
    "Provide a match score from 0 to 100, and a brief explanation of your reasoning.\n\n"
    f"Resume:\n{resume_text}\n\nJob Description:\n{jd_text}\n"
)

try:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    result = response.choices[0].message.content
    with open(output_path, "w", encoding="utf-8") as out:
        out.write(result)
    print(f"Match report saved to '{output_path}'.")
except Exception as e:
    print("Failed to generate match report.")
    print("Error:", e)
