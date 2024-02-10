import toml

def main(toml_path: str):
    pyproject = toml.load(toml_path)
    pyproject["tool"]["poetry"]["version"] = "0.0.1"
    with open(toml_path, "w") as f:
        toml.dump(pyproject, f)
