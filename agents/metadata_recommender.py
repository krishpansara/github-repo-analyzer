from langchain_core.prompts import PromptTemplate
from utils.model import model

prompt_template = PromptTemplate(
        template="""
You are an AI assistant that improves GitHub repository metadata for student projects.

Your task:
- Optimize repository metadata using ONLY the provided information.
- Do NOT invent features, models, datasets, or results.
- Metadata must be honest, clear, and interview-friendly.
- Avoid buzzwords and exaggerated claims.
- Keep everything concise and professional.

--------------------
PROJECT CONTEXT
--------------------

Current Repository Name:
{current_repo_name}

Detected Project Domain:
{project_domain}

--------------------
REPOSITORY STRUCTURE (for context)
--------------------

{repo_structure}

--------------------
EXISTING README SUMMARY (if available)
--------------------

{readme_summary}

--------------------
INSTRUCTIONS
--------------------

1. Suggest an improved repository name:
   - Lowercase
   - Use hyphens (-)
   - Be descriptive but concise
   - Reflect what the project actually does

2. Suggest a short repository description (1–2 lines):
   - Clearly state the problem and solution
   - Mention core technology or approach
   - Avoid vague phrases like "AI powered" unless justified

3. Suggest GitHub topics/tags:
   - Use commonly accepted GitHub topics
   - Prefer technical and domain-specific tags
   - 5–10 tags maximum

4. Suggest important keywords:
   - Useful for search and recruiter scanning
   - Can overlap slightly with topics but be more descriptive

5. If any information is missing or unclear:
   - Make conservative suggestions
   - Do not guess or exaggerate

--------------------
OUTPUT FORMAT (STRICT)
--------------------

Return the output in the following JSON format ONLY:

{{
  "optimized_repo_name": "",
  "repo_description": "",
  "github_topics": [],
  "keywords": []
}}
""",
   input_variables=["current_repo_name", "project_domain", "repo_structure", "readme_summary"],

)

def metadata_recommender(state):
    """
    Suggests improved GitHub repository metadata.
    """

    formatted_prompt = prompt_template.format(
        current_repo_name=state.get("repo_name", ""),
        project_domain=", ".join(state.get("project_domain_signals", [])),
        repo_structure=state.get("structure", ""),
        readme_summary=state.get("readme_summary", "")
    )

    response = model.invoke(formatted_prompt)

    state["metadata"] = response.content

    return state
