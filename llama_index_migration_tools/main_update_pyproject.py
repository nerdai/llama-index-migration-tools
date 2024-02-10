from typing import Dict
from .update_pyproject_toml import update_pyproject_toml
import json
import os


def main():
    # pyproject.tomls list
    with open(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "llamaindex_registry.txt"
        ),
    "r") as f:
        list = f.read().split('\n')
    
    # version_registry
    with open(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "version_registry.json"
        ),
    "r") as f:
        version_registry = json.load(f)

    for package in list:
        if not package:
            continue
        print(package)
        toml_path = os.path.join(package, "pyproject.toml")
        update_pyproject_toml(toml_path=toml_path, version_registry=version_registry)


if __name__ == "__main__":
    main()