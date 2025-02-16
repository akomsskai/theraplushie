import typer
from microphone.recorder import ConversationRecorder

app = typer.Typer()


@app.command()
def run():
    # Create recorder with default settings
    recorder = ConversationRecorder()

    # Start listening
    recorder.listen()


def entrypoint():
    app()
