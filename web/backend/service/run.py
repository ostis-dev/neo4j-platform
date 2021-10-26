import argparse
import os

from .app import App


def main():
    parser = argparse.ArgumentParser(
        description="Initialize database with core elements"
    )
    parser.add_argument("--config", type=str, required=True, help="Path to config file")
    args = parser.parse_args()

    os.environ["CONFIG_PATH"] = args.config

    app = App(args=args)
    app.run()
