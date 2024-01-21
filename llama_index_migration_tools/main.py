import os
import shutil
from pathlib import Path
from templates import pyproject_str, readme_str

def _create_init_file(dir: str):
    # create __init__.py
    Path(dir + "/__init__.py").touch() 

def _makedirs(dir: str):
    try:
        os.makedirs(dir)
    except FileExistsError as e:
        pass


def main(integration_type: str, integration_name: str):
    # create new directory, works in current directory
    pkg_name = f"llama-index-{integration_type}-{integration_name}".replace(" ", "-")
    print(pkg_name)
    pkg_path = os.path.join(os.getcwd(), pkg_name)
    tests_path = os.path.join(pkg_path, "tests")
    examples_path = os.path.join(pkg_path, "examples")
    pkg_src_dir = os.path.join(
        pkg_path,
        f"llama_index/{integration_type.replace('-', '_')}/{integration_name.replace('-', '_')}"
    )

    # make dirs
    _makedirs(pkg_path)
    _makedirs(tests_path)
    _makedirs(examples_path)
    _makedirs(pkg_src_dir)

    # create init files
    _create_init_file(tests_path)
    _create_init_file(pkg_src_dir)

    # ceate readme and pyproject.toml
    with open(pkg_path + "/pyproject.toml", "w") as f:
        f.write(
            pyproject_str.format(
                PACKAGE_NAME=pkg_name,
                TYPE=integration_type,
                NAME=integration_name
            )
        )

if __name__ == "__main__":
    main("test", "test pkg")
