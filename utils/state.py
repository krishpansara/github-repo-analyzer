from typing import TypedDict, Optional, List, Dict, Any

class State(TypedDict):
    repo_url: str
    repo_name: str
    project_description: Optional[str]
    readme_content: Optional[str]
    structure: Optional[str]
    project_domain_signals: Optional[List[str]]
    updated_readme: Optional[str]
    readme_summary: Optional[str]
    metadata: Optional[str]
    reviewer_feedback: Optional[str]
