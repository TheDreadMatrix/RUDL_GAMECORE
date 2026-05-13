
import os


def main():
    # Set default name for the project
    # Also do not touch that environ!!! You can destroy your project!!!
    os.environ.setdefault("RUDLGC_PROJECT_NAME", "DaemonDuck16")


    try:
        # Import your CLI executor here
        from rudlgc.core.execute_prompt import execute_console
    except ImportError as exc:
        raise ImportError(
            "Couldn't import RUDLGC. Are you sure it's installed? Did you forget to activate a virtual environment?"
        ) from exc

    # Pass CLI arguments to your engine
    execute_console()


if __name__ == "__main__":
    main()
