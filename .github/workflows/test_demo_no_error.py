#!/bin/python3

from os import system
from pathlib import Path


# This script is meant to run on GitHub's virtual machine ubuntu-latest in a
# CI workflow. It runs the repository's demo to ensure that no error occurs.

repo_root = Path(__file__).resolve().parents[2]

system(f"python3 {repo_root}/demo.py")
