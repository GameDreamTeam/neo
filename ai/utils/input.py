import sys


def read_stdin():
    if not sys.stdin.isatty():
        return sys.stdin.read()
    return None
