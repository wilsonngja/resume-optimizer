import os
import markdown
import fitz
from openai import OpenAI
from weasyprint import HTML


client = OpenAI()

resume_text = ""
folder_path = "./data"

for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(folder_path, filename)
        with fitz.open(pdf_path) as doc:
            resume_text += "\n".join(page.get_text("text") for page in doc)


role = input("What role are you applying for: ")

query_content = f"Help me to optimize my resume for the role of ${role} based on my current resume in markdown format:\n${resume_text}.\nThe output should only contain information relevant to the resume. Additionally, do pick out what is best related to the field, removing unnecessary information. You should not add additional information that is excessive."

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
HTML(string=html).write_pdf("output.pdf")
