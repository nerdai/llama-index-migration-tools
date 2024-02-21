from typing import Dict, List
import toml

PYTHON_DEPENDENCY_REQ = '>=3.8.1,<4.0'

def update_pyproject_toml(toml_path: str, version_registry: Dict[str, str]):
    pyproject = toml.load(toml_path)
    poetry_config = pyproject["tool"]["poetry"]

    # update version according to version_registry
    package_name = poetry_config["name"]
    pyproject["tool"]["poetry"]["version"] = version_registry[package_name]

    # update llama-index package versions in list of deps
    dependencies = poetry_config["dependencies"]
    for dep in dependencies.keys():
        if dep in version_registry:
            dependencies[dep] = "^" + version_registry[dep]

    with open(toml_path, "w") as f:
        toml.dump(pyproject, f)


def add_llamahub_metadata(toml_path: str, import_path: str, classes: List[str], contains_example: bool):
    pyproject = toml.load(toml_path)

    # add llamahub metadata
    pyproject["tool"]["llamahub"] = {}
    pyproject["tool"]["llamahub"]["class_authors"] = {c: "llama-index" for c in classes}
    pyproject["tool"]["llamahub"]["import_path"] = import_path
    pyproject["tool"]["llamahub"]["contains_example"] = contains_example

    with open(toml_path, "w") as f:
        toml.dump(pyproject, f)


def update_python_req_add_exclusion_of_build(toml_path: str):
    pyproject = toml.load(toml_path)
    poetry_config = pyproject["tool"]["poetry"]

    # update python req
    poetry_config['dependencies']['python'] = PYTHON_DEPENDENCY_REQ

    # add exclusion of BUILD
    if "exclude" in poetry_config:
        poetry_config['exclude'] += ["**/BUILD"]
    else:
        poetry_config['exclude'] = ["**/BUILD"]

    with open(toml_path, "w") as f:
        toml.dump(pyproject, f)
