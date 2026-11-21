from app.graph.state import CodeGuardianState
import os


import os

def repository_scanner(state: CodeGuardianState):
    print("Scanning repository...")

    repo_path = state["repo_path"]

    supported_extensions = {
        ".py", ".js", ".java", ".cpp", ".c",
        ".rb", ".go", ".ts", ".php", ".cs",
        ".swift", ".kt", ".rs", ".m", ".scala",
        ".pl", ".sh"
    }

    excluded_dirs = {
        ".git", "__pycache__", "node_modules",
        "venv", "build", "dist"
    }

    discovered_files = []

    for root, dirs, files in os.walk(repo_path):

        dirs[:] = [d for d in dirs if d not in excluded_dirs]

        for file in files:

            extension = os.path.splitext(file)[1].lower()

            valid_file = extension in supported_extensions

            if valid_file:
                file_absolute_path = os.path.join(root, file)

                file_relative_path = os.path.relpath(
                    file_absolute_path, repo_path
                )

                discovered_files.append(file_relative_path)

    print(f"Discovered {len(discovered_files)} files: {discovered_files}")

    return {
        "files": discovered_files
    }


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