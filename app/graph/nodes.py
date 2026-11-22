from app.graph.state import CodeGuardianState
from app.utils.file_reader import read_file, is_file_too_large


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

def file_reader_node(state: CodeGuardianState):
    print("Reading repository files...")

    repo_path = state["repo_path"]
    files = state["files"]

    file_contents = {}
    skipped_files = []

    for file_path in files:
        absolute_path = os.path.join(repo_path, file_path)

        if is_file_too_large(absolute_path):
            print(f"Skipping large file: {file_path}")
            skipped_files.append(file_path)
            continue

        code = read_file(absolute_path)

        file_contents[file_path] = code

    print(f"Successfully read {len(file_contents)} files.")
    print(f"Skipped {len(skipped_files)} large files.")

    return {
    "file_contents": file_contents,
    "skipped_files": skipped_files
}