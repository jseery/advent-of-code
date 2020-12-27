from pathlib import Path
import inspect


def get_inputs_dir():
    return Path(__file__).parent.joinpath("inputs")


def get_puzzle_input(fname: str) -> str:

    frame = inspect.stack()[1]
    caller_filename = Path(frame[0].f_code.co_filename).stem
    input = get_inputs_dir().joinpath(caller_filename, fname).read_text()
    return input
