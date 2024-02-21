from typing import Dict
from ..lib.update_pyproject_toml import update_python_req_add_exclusion_of_build 
import json
import os

IGNORE_LIST = [
    "/Users/nerdai/Projects/llama_index/llama-index-experimental",
    "/Users/nerdai/Projects/llama_index/llama-index-core",
    "/Users/nerdai/Projects/llama_index",
    "/Users/nerdai/Projects/llama_index/llama-index-legacy",
    "/Users/nerdai/Projects/llama_index/llama-index-finetuning",
    "/Users/nerdai/Projects/llama_index/llama-index-cli",
    "/Users/nerdai/Projects/llama_index/llama-index-core/notebooks/pack"
]


def main():
    # pyproject.tomls list
    with open(
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "llamaindex_registry.txt"
        ),
    "r") as f:
        list = f.read().split('\n')
    
    for package in list:
        if not package:
            continue
        if package in IGNORE_LIST:
            continue
        print(package)
        toml_path = os.path.join(package, "pyproject.toml")
        update_python_req_add_exclusion_of_build(toml_path=toml_path)


if __name__ == "__main__":
    main()