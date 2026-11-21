from typing import TypedDict


class CodeGuardianState(TypedDict):
    """
    CodeGuardianState is a shareable state object
    used to store the state of the CodeGuardian application.
    """
    repo_path: str
    files: list[str]
    bugs: list[str]
    security_issues: list[str]
    file_summary: str
