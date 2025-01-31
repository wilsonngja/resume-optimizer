# resume-optimizer

## About this project
This project aims to perform optimisation on resumes for a specific roles, extracting relevant information to the role inputted by the user when prompted. This project was build on Python version `3.13`.

OpenAI's `gpt-4o` is selected to generate the resume.

## Tech Stack
The tech stack used in this project are as follows:
- Python Markdown (Rendering Markdown element into HTML)
- Fitz (Processing PDF files)
- OpenAI API (For text completion features)
- WeasyPrint (Saving a HTML file as PDF)

The `WeasyPrint` library is used because a standalone markdown string cannot be saved to render a PDF file. Therefore, an additional requirement to convert markdown -> HTML and from HTML -> PDF is required.

## Setting Up
To begin the setup, install the relevant dependencies using the following command:
`pip install -r requirements.txt`.


### OpenAI API Key
To acquire an API Key from OpenAI visit the website: [here](https://platform.openai.com/docs/overview)

A quick and temporary solution is to replace the code in `main.py` from the following:

```
client = OpenAI()
```

to 

```
client = OpenAI(api_key="your_api_key_here")
```

This is not recommendated due to potential security risk.

Another approach is to set the API Key as environmental variable. For a Mac machine it's done as follows in a virtual environment (conda):

```
conda env config vars set OPENAI_API_KEY="your-api-key-here"
conda activate resume-optimizer
```

## Usage
For the application to work, insert at least one resume in `.pdf` format inside the `data` directory. However, to better response, do insert multiple resume, consisting of different experience to allow the model to select the more important information.

Start the application by running: `python main.py`

Do wait for about 30 second for the document to be created. 
