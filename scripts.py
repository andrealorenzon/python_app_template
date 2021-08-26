import sys
from subprocess import CalledProcessError, check_call

def _check_call_quiet(commands: list[str], *, shell: bool=False) -> None:
    try:
        check_call(commands, shell=shell)
    except CalledProcessError as error:
        sys.exit(error.returncode)


def format() -> None:
    _check_call_quiet(["black", "--check", "--diff", "app/src/", "app/tests/"])

def reformat() -> None:
    _check_call_quiet(["black", "app/src/", "app/tests/"])
    
def lint() -> None:
    _check_call_quiet(["mypy", "app/src/", "app/tests/"])
    _check_call_quiet(["flake8", "app/src/", "app/tests/"])
    _check_call_quiet(["vulture", "app/src/"])
    _check_call_quiet(["bandit", "-r", "app/src/"])

def test() -> None: 
    _check_call_quiet(["pytest", "app/tests/", *sys.argv[1:]])