from app.graph.state import CodeGuardianState
import os


def repository_scanner(state: CodeGuardianState):
    print("Scanning repository...")

    # print("Repository path:", state["repo_path"])

    # return {
    #     "files": ["main.py", "database.py", "auth.py"]
    # }


def file_summary_node(state: CodeGuardianState):
    print("File Summary Node: Reading scanner output...")

    files = state["files"]

    summary = f"Scanner discovered {len(files)} files: {', '.join(files)}"

    print(summary)

    return {
        "file_summary": summary
    }

def route_after_scan(state: CodeGuardianState):
    files = state["files"]

    if len(files) > 0:
        return ["code_analysis", "security_analysis"]

    return "end"

def code_analysis_node(state: CodeGuardianState):
    print("Code Analysis Agent: Analyzing code...")

    return {
        "bugs": ["Potential logical error detected"]
    }

def security_analysis_node(state: CodeGuardianState):
    print("Security Analysis Agent: Analyzing security...")

    return {
        "security_issues": ["Potential security vulnerability detected"]
    }