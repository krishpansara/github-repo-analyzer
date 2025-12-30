from urllib.parse import urlparse

def extract_repo_info(state) -> dict:
    """
    Extracts owner and repository name from a GitHub URL.
    """
    repo_url = state["repo_url"]
    parsed = urlparse(repo_url)
    print(f" parsed : {parsed}")
    path_parts = parsed.path.strip("/").split("/")
    print(f" path_parts : {path_parts}")


    if len(path_parts) < 2:
        raise ValueError("Invalid GitHub repository URL")

    repo = path_parts[1].replace(".git", "")

    state["repo_name"] = repo

    return state
