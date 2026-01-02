from git import Repo
import os, shutil, stat

REPO_DIR = "TEMP_CLONE_PATH"

def force_delete(func, path, _):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def repo_extractor(state):
    '''
    This is the repo analyzer function.
    Which analyze repo by extracting readme file and the sturucture of the Repo 
    '''
    repo_url = state["repo_url"]

    # checks if repo already cloned or not
    if os.path.exists(REPO_DIR):
        shutil.rmtree(REPO_DIR, onerror=force_delete)

    # clon the repo
    Repo.clone_from(repo_url, REPO_DIR)

    # if the readme file is present extract it's contents
    readme_path = os.path.join(REPO_DIR, "README.md")
    readme_file = open(readme_path, encoding="utf-8").read() if os.path.exists(readme_path) else "No README.md file found."

    # extracts the structure of the repo (all files location)
    structure = "\n".join(os.path.relpath(r, REPO_DIR) for r,_,_ in os.walk(REPO_DIR))

    state["readme_file"]= readme_file
    state["structure"]= structure

    return state

