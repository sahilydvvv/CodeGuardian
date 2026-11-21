from app.graph.workflow import graph


initial_state = {
    "repo_path": "my_project",
    "files": [],
    "bugs": [],
    "security_issues": [],
    "file_summary": ""
}


result = graph.invoke(initial_state)


print("\nFinal State:")
print(result)