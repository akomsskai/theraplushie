import typer

from core import return_two
from core.main import plushieProtocol

app = typer.Typer()


@app.command()
def run():
    print(f"Here is {return_two()} for you")

    plushieProtocol()


def entrypoint():
    app()
