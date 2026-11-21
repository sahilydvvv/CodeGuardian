from app.graph.nodes import repository_scanner


initial_state = {
    "repo_path": "my_project",
    "files": [],
    "bugs": [],
    "security_issues": []
}


result = repository_scanner(initial_state)

print("Node output:", result)