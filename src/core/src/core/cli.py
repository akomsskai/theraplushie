import typer

from core import return_two
from core.main import plushieProtocol

app = typer.Typer()


@app.command()
def run():
    
    plushieProtocol()


def entrypoint():
    app()
