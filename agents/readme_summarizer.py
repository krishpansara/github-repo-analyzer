from utils.model import model
from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate(
        template="""
You are an AI assistant that summarizes GitHub README files for student projects.

Your task:
- Create a concise summary based ONLY on the provided README content.
- Do NOT invent features, models, datasets, or results.
- Use clear, professional, student-friendly language.
- Avoid buzzwords and marketing phrases.
- Keep the summary suitable for recruiters and interviewers.

--------------------
UPDATED README CONTENT
--------------------

{updated_readme}

--------------------
Project Description (Optional)
--------------------

{project_description}

--------------------
INSTRUCTIONS
--------------------

1. Summarize the README in 3–5 sentences.
2. Clearly state:
   - What the project does
   - The problem it addresses
   - The core technology or approach used
3. If certain details are missing, do not guess.
4. Keep the tone factual and confident, not promotional.
5. Do NOT include code blocks, emojis, or Markdown formatting.

----
""",
input_variables=["updated_readme", "project_description"]
    )    


def readme_summarizer(state):
    """
    Generates a concise recruiter-friendly summary from the updated README.
    """

    updated_readme = state.get("updated_readme", "")
    project_description = state.get("project_description", "")

    
    formatted_prompt = prompt_template.format(
        updated_readme=updated_readme,
        project_description=project_description
    )

    response = model.invoke(formatted_prompt)

    state["readme_summary"] = response.content

    return state