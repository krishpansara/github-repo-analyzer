from langchain_core.prompts import PromptTemplate
from utils.model import model


prompt_template = PromptTemplate(
    template="""
You are an expert open-source reviewer rewriting a GitHub README for a student project.

Your responsibility:
- Produce a README that would be acceptable in a technical interview.
- Be honest but firm.
- Clearly distinguish between:
  • Implemented features
  • Planned features
  • Missing components
- If code is missing, explicitly state that the project is currently conceptual or incomplete.

CRITICAL RULES:
- Do NOT invent code, features, datasets, or results.
- Do NOT hide missing implementation.
- If the repository lacks source files, say so clearly.
- The README must still look professional and structured.

--------------------
PROJECT CONTEXT
--------------------

Repository Name:
{repo_name}

Repository Structure:
{repo_structure}

--------------------
EXISTING README
--------------------

{existing_readme}

--------------------
INSTRUCTIONS
--------------------

Rewrite the README so that it includes ALL of the following sections:

1. Project Overview  
   - What problem the project aims to solve.
   - Whether the project is implemented or currently in planning.

2. Current Status (MANDATORY)
   - Clearly state what is implemented.
   - Clearly state what is NOT implemented.

3. Planned Features
   - Bullet list of features intended for future development.

4. Intended Architecture / Workflow
   - High-level explanation (no fake technical depth).

5. Tech Stack
   - Only technologies explicitly mentioned or implied.

6. Installation
   - If not runnable yet, explicitly say so.

7. Usage
   - If no usage exists, explain why.

8. Limitations
   - Be honest and specific.

9. Next Steps
   - Concrete, actionable next development steps.

Tone:
- Professional
- Direct
- Honest
- Interview-ready
- No emojis
- No hype

--------------------
OUTPUT
--------------------

Return ONLY the rewritten README in valid Markdown.


        """,
    input_variables = ['repo_name', 'repo_structure', 'project_description', 'existing_readme'],

)


def content_improver(state):
    """
    Improves or generates README content based on repo evidence.
    """

    existing_readme = state.get('readme_file', "")
    project_description = state.get("project_description", "")
    repo_name = state.get("repo_name", "")
    repo_structure = state.get("structure", "")

    formatted_prompt = prompt_template.format(
        repo_name=repo_name,
        repo_structure=repo_structure,
        project_description=project_description,
        existing_readme=existing_readme
    )

    response = model.invoke(formatted_prompt)

    state["updated_readme"] = response.content

    return state