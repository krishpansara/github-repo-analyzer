from langgraph.graph import StateGraph, START, END
from .state import State

from agents.repo_extractor import repo_extractor
from agents.content_improver import content_improver
from agents.readme_summarizer import readme_summarizer
from agents.metadata_recommender import metadata_recommender
from agents.reviewer import reviewer


def create_graph():
    workflow = StateGraph(State)
    workflow.add_node("repo_extractor", repo_extractor)
    workflow.add_node("content_improver", content_improver)
    workflow.add_node("readme_summarizer", readme_summarizer)
    workflow.add_node("metadata_recommender", metadata_recommender)
    workflow.add_node("reviewer", reviewer)

    workflow.add_edge(START, "repo_extractor")
    workflow.add_edge("repo_extractor", "content_improver")
    workflow.add_edge("content_improver", "readme_summarizer")
    workflow.add_edge("readme_summarizer", "metadata_recommender")
    workflow.add_edge("metadata_recommender", "reviewer")
    workflow.add_edge("reviewer", END)

    return workflow.compile()
