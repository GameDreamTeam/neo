import typer
from rich.console import Console
from rich.prompt import Prompt
from ai.llm.ollama_client import OllamaClient

console = Console()


def chat():
    """
    Interactive chat session.
    """
    client = OllamaClient()

    console.print("[bold green]AI Chat[/bold green] (type 'exit' to quit)\n")

    messages = [
        {
            "role": "system",
            "content": "You are a senior DevOps engineer assistant. Be concise and actionable."
        }
    ]

    try:
        while True:
            user_input = Prompt.ask("[bold cyan]You[/bold cyan]")

            if user_input.lower() in {"exit", "quit"}:
                console.print("\n[bold red]Goodbye![/bold red]")
                break

            messages.append({
                "role": "user",
                "content": user_input
            })

            console.print("\n[bold yellow]AI[/bold yellow]: ", end="")

            response_chunks = []
            for chunk in client.stream(messages):
                console.print(chunk, end="", soft_wrap=True)
                response_chunks.append(chunk)

            console.print("\n")

            messages.append({
                "role": "assistant",
                "content": "".join(response_chunks)
            })

    except KeyboardInterrupt:
        console.print("\n\n[bold red]Session terminated.[/bold red]")
