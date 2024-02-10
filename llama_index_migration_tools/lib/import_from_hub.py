import os
import shutil
from distutils import dir_util
from pathlib import Path
from llama_index_migration_tools.templates import pyproject_str, readme_str, init_str, init_with_prefix_str
from typing import Optional

def _create_init_file(dir: str):
    # create __init__.py
    Path(dir + "/__init__.py").touch() 

def _create_test_file(filename: str):
    Path(filename).touch()

def _makedirs(dir: str):
    try:
        os.makedirs(dir)
    except FileExistsError as e:
        pass


def main_hub(integration_type: str, integration_name: str, hub_path: str):
    # create new directory, works in current directory
    pkg_name = f"llama-index-{integration_type}-{integration_name}".replace(" ", "-").replace("_", "-").lower()
    pkg_path = os.path.join(os.getcwd(), pkg_name)
    tests_path = os.path.join(pkg_path, "tests")
    examples_path = os.path.join(pkg_path, "examples")
    pkg_src_dir = os.path.join(
        pkg_path,
        f"llama_index/{integration_type}/{integration_name}".replace(' ', '_').lower()
    )

    # make dirs
    _makedirs(pkg_path)
    _makedirs(tests_path)
    _makedirs(examples_path)
    _makedirs(pkg_src_dir)

    # create init files
    _create_init_file(tests_path)
    
    # create pyproject.toml
    with open(pkg_path + "/pyproject.toml", "w") as f:
        f.write(
            pyproject_str.format(
                PACKAGE_NAME=pkg_name,
                TYPE=integration_type.lower(),
                NAME=integration_name.lower()
            )
        )
    
    # create an empty test file
    test_file_name = tests_path + f"/test_{integration_type}_{integration_name}.py".replace(" ", "_").lower()
    _create_test_file(test_file_name)
    
    # copy common files to folders
    script_path = Path(__file__).parent.resolve()
    common_path = os.path.join(script_path, "common")
    shutil.copyfile(common_path + "/.gitignore", pkg_path + "/.gitignore")
    shutil.copyfile(common_path + "/Makefile", pkg_path + "/Makefile")

    # copy llama hub dir contents
    dir_util.copy_tree(hub_path, pkg_src_dir)
    shutil.move(pkg_src_dir + "/README.md", pkg_path + "/README.md")
    shutil.move(pkg_src_dir + "/requirements.txt", pkg_path + "/requirements.txt")
    # overwrite init
    with open(pkg_src_dir + "/__init__.py", "w") as f:
        init_string = init_str.format(
            TYPE=integration_type.replace(" ", "_").lower(),
            NAME=integration_name.replace(" ", "_").lower(),
        )
        f.write(init_string)
