
# %%

# Ensure the root directory is in the path for imports
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from aisb_utils import report

# Common imports
import requests
from typing import Callable

print("It works!")

# %%
from day0_test import test_prerequisites


# Run the prerequisite checks
test_prerequisites()

# %%

from dataclasses import dataclass


@dataclass
class UserIntel:
    username: str
    name: str | None
    location: str | None
    email: str | None
    repo_names: list[str]


def analyze_user_behavior(username: str = "karpathy") -> UserIntel:
    """
    Analyze a user's GitHub activity patterns.
    This is the kind of profiling attackers might do for social engineering.

    Returns:
        The user's name, location, email, and 5 most recently updated repos.
    """
    response = requests.get(f"https://api.github.com/users/{username}")

    if not response.ok:
        return UserIntel(
            username=username,
            name=None,
            location=None,
            email=None,
            repo_names=[]
        )

    content = response.json()
    name, location, email = content["name"], content["location"], content["email"]

    response = requests.get(f"https://api.github.com/users/{username}/repos?sort=updated&per_page=5")
    content = response.json()
    repo_names = [c['name'] for c in content]

    return UserIntel(
        username=username,
        name=name,
        location=location,
        email=email,
        repo_names=repo_names
    )
from day0_test import test_analyze_user_behavior


test_analyze_user_behavior(analyze_user_behavior)

# %%
