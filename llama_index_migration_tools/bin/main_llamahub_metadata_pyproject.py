import os
from typing import List
from ..lib.update_pyproject_toml import add_llamahub_metadata

def _get_namespaces(package_path: str):
    walker = os.walk(os.path.join(package_path, "llama_index"))
    namespaces = ["llama_index"]
    
    found_init = False
    while not found_init:
        _, dirs, files = next(walker)
        if "__init__.py" in files:
            found_init = True
        else:
            namespaces += dirs
            
    return namespaces


def _get_all_imports(package_path: str, namespaces: List[str]) -> List[str]:
    namespace = os.path.join(*namespaces)
    with open(os.path.join(package_path, *[namespace, "__init__.py"]), "r") as f:
        init = f.read()
    if "__all__" in init:
        return eval(init.split("__all__")[-1].replace("=",""))
    else:
        return []

def main():
    # load package index
    with open(
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "llamaindex_registry.txt"
        ),
    "r") as f:
        list = f.read().split('\n')

    for package_path in list:
        if not package_path:
            continue
        print(package_path)

        # toml path
        toml_path = os.path.join(package_path, "pyproject.toml")

        # import path    
        namespaces = []
        if not package_path.endswith("llama_index"):
            namespaces = _get_namespaces(package_path)
        if namespaces:
            import_path = os.path.join(*namespaces).replace("/", ".")

        # classes
        classes = []
        if not (
            package_path.endswith("llama_index")
            or package_path.endswith("llama-index-core")
            or package_path.endswith("llama-index-legacy")
            or not package_path
        ):
            classes = _get_all_imports(package_path, namespaces)

        # contains example.py
        contains_example = os.path.isfile(
            os.path.join(package_path, "examples/example.py")
        )

        add_llamahub_metadata(
            toml_path=toml_path,
            import_path=import_path,
            classes=classes,
            contains_example=contains_example
        )


if __name__ == "__main__":
    main()