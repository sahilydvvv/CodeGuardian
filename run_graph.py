from app.graph.workflow import graph


initial_state = {
    "repo_path": "sample_repo",
    "files": [],
    "bugs": [],
    "security_issues": [],
    "file_summary": ""
}


result = graph.invoke(initial_state)


print("\nFinal State:")
print(result)