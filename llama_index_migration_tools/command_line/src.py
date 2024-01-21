import argparse
from typing import Any

from llama_index_migration_tools.main import main as init_package

def handle_init_package(
    name: str,
    kind: str
):
    init_package(integration_name=name, integration_type=kind)
    print(f"Successfully initialized package")


def main() -> None:
    parser = argparse.ArgumentParser(description="LlamaIndex Migration CLI tool.")

    # Subparsers for the main commands
    subparsers = parser.add_subparsers(title="commands", dest="command", required=True)

    # init package command
    init_parser = subparsers.add_parser(
        "init-package", help="Initialize a llama-index package"
    )
    init_parser.add_argument(
        "-k",
        "--kind",
        type=str,
        help="Kind of package, e.g., integration, plugin, etc."
    )
    init_parser.add_argument(
        "-n",
        "--name",
        type=str,
        help="Name of python package",
    )
    init_parser.set_defaults(
        func=lambda args: handle_init_package(**vars(args))
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the appropriate function based on the command
    args.func(args)


if __name__ == "__main__":
    main()
