from langgraph.graph import StateGraph, START, END

from app.graph.state import CodeGuardianState
from app.graph.nodes import (
    repository_scanner,
    file_summary_node,
    route_after_scan,
    code_analysis_node,
    security_analysis_node,
    file_reader_node
)


builder = StateGraph(CodeGuardianState)

builder.add_node("scanner", repository_scanner)
builder.add_node("file_summary", file_summary_node)
builder.add_node("code_analysis", code_analysis_node)
builder.add_node("security_analysis", security_analysis_node)
builder.add_node("file_reader", file_reader_node)


builder.add_edge(START, "scanner")

builder.add_edge("scanner", "file_reader")

builder.add_conditional_edges(
    "file_reader",
    route_after_scan,
    {
        "code_analysis": "code_analysis",
        "security_analysis": "security_analysis",
        "end": END
    }
)


builder.add_edge(
    ["code_analysis", "security_analysis"],
    "file_summary"
)


builder.add_edge("file_summary", END)


graph = builder.compile()