from app.graph.workflow import graph


initial_state = {
    "repo_path": "sample_repo",
    "files": [],
    "file_contents": {},
    "bugs": [],
    "security_issues": [],
    "file_summary": "",
    "skipped_files": []
}


result = graph.invoke(initial_state)


print("\nFinal State:")
print(result)