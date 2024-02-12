from typing import Dict
import toml

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
