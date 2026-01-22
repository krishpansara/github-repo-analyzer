from langchain_core.prompts import PromptTemplate
from utils.model import model
from utils.json_parser import safe_json_parse

REVIEWER_PROMPT = PromptTemplate(
    input_variables=[
        "repo_name",
        "primary_language",
        "tech_stack",
        "project_domain",
        "repo_structure",
        "updated_readme"
    ],
    template="""
You are a senior software engineer and interviewer reviewing a student's GitHub repository.

Your task:
- Critically review the repository based ONLY on the provided information.
- Do NOT invent features, results, or implementation details.
- Evaluate clarity, completeness, and technical understanding.
- Think like a recruiter who has 2–3 minutes to scan a repo.

--------------------
PROJECT CONTEXT
--------------------

Repository Name:
{repo_name}

Primary Language:
{primary_language}

Detected Tech Stack:
{tech_stack}

Project Domain:
{project_domain}

--------------------
REPOSITORY STRUCTURE
--------------------

{repo_structure}

--------------------
UPDATED README
--------------------

{updated_readme}

--------------------
INSTRUCTIONS
--------------------

1. Evaluate the repository on the following aspects:
   - Clarity of problem statement
   - Explanation of how the project works
   - Technical correctness (based on claims)
   - Documentation completeness
   - Overall professionalism

2. Identify:
   - Key strengths
   - Key weaknesses
   - Missing or unclear sections

3. Assign an overall interview readiness score from 1 to 10.

4. Based on your review, classify the hire signal as:
   - "Low"
   - "Medium"
   - "High"

5. Be honest, constructive, and specific.

--------------------
OUTPUT FORMAT (STRICT JSON)
--------------------
IMPORTANT:
- You MUST return a COMPLETE and VALID JSON object.
- Do NOT include explanations, markdown, or extra text.
- Ensure all strings, arrays, and braces are properly closed.


{{
  "interview_score": 0,
  "hire_signal": "",
  "strengths": [],
  "weaknesses": [],
  "missing_sections": [],
  "actionable_suggestions": []
}}
"""
)

def reviewer(state):
    """
    Reviewer / Interviewer Agent
    """
    # llm = ChatOpenAI(temperature=0)

    prompt = REVIEWER_PROMPT.format(
        repo_name=state.get("repo_name", ""),
        primary_language=state.get("primary_language", ""),
        tech_stack=", ".join(state.get("tech_stack", [])),
        project_domain=", ".join(state.get("project_domain_signals", [])),
        repo_structure=state.get("structure", ""),
        updated_readme=state.get("updated_readme", "")
    )

    response = model.invoke(prompt)
    parsed = safe_json_parse(response.content)

    if parsed is None:
        state["reviewer_feedback"] = {
            "error": "Reviewer output could not be parsed",
            "raw_output": response.content
        }
    else:
        state["reviewer_feedback"] = parsed

    return state