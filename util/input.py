from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent

def get_input(year: int, exercise: int) -> str:
    """
    Always returns with a trailing newline
    """
    input_path = REPO_ROOT / f'{year}/data/ex_{exercise}.txt'
    return input_path.read_text()
