import pathlib


def load_prompt():
    """Loads the main review prompt from a file."""
    with open(pathlib.Path(__file__).parent / 'prompt.txt',
              encoding='utf-8') as fp:
        return fp.read()
