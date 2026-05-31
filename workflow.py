from typing import TypedDict
from langgraph.graph import StateGraph, END

from agents import (
    topic_agent,
    summary_agent,
    action_agent,
    priority_agent
)

class MeetingState(TypedDict):

    transcript: str

    topics: str

    summary: str

    actions: str

    priority: str


def topic_node(state):

    state["topics"] = topic_agent(
        state["transcript"]
    )

    return state


def summary_node(state):

    state["summary"] = summary_agent(
        state["transcript"]
    )

    return state


def action_node(state):

    state["actions"] = action_agent(
        state["transcript"]
    )

    return state


def priority_node(state):

    state["priority"] = priority_agent(
        state["transcript"]
    )

    return state


def skip_priority_node(state):

    state["priority"] = (
        "No action items identified."
    )

    return state


def check_actions(state):

    if "NO ACTION ITEMS" in state["actions"]:
        return "skip_priority"

    return "run_priority"


workflow = StateGraph(
    MeetingState
)

workflow.add_node(
    "topics",
    topic_node
)

workflow.add_node(
    "summary",
    summary_node
)

workflow.add_node(
    "actions",
    action_node
)

workflow.add_node(
    "priority",
    priority_node
)

workflow.add_node(
    "skip_priority",
    skip_priority_node
)

workflow.set_entry_point(
    "topics"
)

workflow.add_edge(
    "topics",
    "summary"
)

workflow.add_edge(
    "summary",
    "actions"
)

workflow.add_conditional_edges(
    "actions",
    check_actions,
    {
        "run_priority": "priority",
        "skip_priority": "skip_priority"
    }
)

workflow.add_edge(
    "priority",
    END
)

workflow.add_edge(
    "skip_priority",
    END
)

graph = workflow.compile()
