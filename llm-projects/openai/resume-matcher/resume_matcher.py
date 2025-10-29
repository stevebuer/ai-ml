
import openai
import httpx
import os
import sys
import argparse
import pdfplumber

def main():
    parser = argparse.ArgumentParser(description="Resume Matcher")
    parser.add_argument("--resume", required=True, help="Path to resume file (.md or .pdf)")
    parser.add_argument("--jobdesc", required=True, help="Path to job description file")
    parser.add_argument("--output", required=True, help="Path to output match report file")
    parser.add_argument("--model", default="gpt-4o", help="OpenAI model name (default: gpt-4o)")
    args = parser.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("OPENAI_API_KEY environment variable not set.")
        sys.exit(1)

    client = openai.OpenAI(
        api_key=api_key,
        http_client=httpx.Client(verify=False)
    )

    resume_path = args.resume
    jd_path = args.jobdesc
    output_path = args.output

    if not os.path.exists(resume_path):
        print(f"Resume file '{resume_path}' not found.")
        sys.exit(1)

    if resume_path.endswith(".md"):
        with open(resume_path, "r", encoding="utf-8") as f:
            resume_text = f.read()
    elif resume_path.endswith(".pdf"):
        with pdfplumber.open(resume_path) as pdf:
            resume_text = "\n".join(page.extract_text() or "" for page in pdf.pages)
    else:
        print("Resume file must be .md or .pdf format.")
        sys.exit(1)

    if not os.path.exists(jd_path):
        print(f"Job description file '{jd_path}' not found.")
        sys.exit(1)

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
            model=args.model,
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content
        with open(output_path, "w", encoding="utf-8") as out:
            out.write(result)
        print(f"Match report saved to '{output_path}'.")
    except Exception as e:
        print("Failed to generate match report.")
        print("Error:", e)

if __name__ == "__main__":
    main()
