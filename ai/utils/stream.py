from rich.console import Console

console = Console()


def stream_output(generator):
    for chunk in generator:
        console.print(chunk, end="", soft_wrap=True)
    console.print()
