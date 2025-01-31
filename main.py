import os
import markdown
import fitz
from openai import OpenAI
from weasyprint import HTML


client = OpenAI()

resume_text = ""

with fitz.open("resume.pdf") as doc:
    resume_text = "\n".join(page.get_text("text") for page in doc)
# print(os.environ["OPENAI_API_KEY"])

# print(resume_text)

role = input("What role are you applying for: ")

query_content = f"Help me to optimize my resume for the role of ${role} based on my current resume in markdown format:\n${resume_text}.\nThe output should not contain any other things other than the markdown text"

new_resume = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content" : "You are a helpful assistant."},
        {
            "role": "user",
            "content":query_content
        }
    ]
)

html = markdown.markdown(new_resume.choices[0].message.content)
HTML(string=html).write_pdf("output2.pdf")
