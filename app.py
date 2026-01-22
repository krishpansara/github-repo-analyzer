import streamlit as st
import time

from utils.state import State
from utils.graph import create_graph
from utils.repo_name import extract_repo_info
# https://github.com/krishpansara/file_sorting_system


st.set_page_config(
    page_title="GitMate",
    layout="wide"
)

st.markdown("<h1 style='text-align:center;'>GitMate</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align:center;'>The Mullti Agent System that will help you to the Enhance your GitHub Reposetory</h5>", unsafe_allow_html=True)


repo_url = st.text_input("Enter GitHub Repo Link : ")
project_description = st.text_area("(Optional) Enter brief detail about your Project")

if st.button("🔍 Analyze and Improve") and repo_url:
    
    start_time = time.time()
    initial_state: State = {"repo_url":repo_url, "project_description":project_description}
    repo_info = extract_repo_info(initial_state)

    graph = create_graph()
    final_state = graph.invoke(initial_state)

    st.success(f"Completed in {time.time() - start_time:.2f}s")

    st.divider()

    st.subheader("📘 Improved README (Preview)")
    st.markdown(final_state.get("updated_readme", ""))

    st.divider()

    st.subheader("🧾 Raw README (Markdown)")
    st.text_area(
        label="Copy this Markdown and paste directly into GitHub",
        value=final_state["updated_readme"],
        height=400
    )


    st.subheader("🧠 README Summary")
    st.write(final_state.get("readme_summary", ""))

    st.divider()

    st.subheader("🏷️ Suggested Metadata")
    st.json(final_state.get("metadata", {}))

    st.divider()

    st.subheader("🎯 Interviewer Review")
    # st.json(final_state.get("reviewer_feedback", {}))
    review = final_state.get("reviewer_feedback")

    if isinstance(review, dict):
        st.json(review)
    else:
        st.error("Reviewer output could not be parsed")
        st.text(review)
