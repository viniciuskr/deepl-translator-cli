import os
import sys
import deepl
import typer
from dotenv import load_dotenv
from typing import Optional

import language_tool_python

# Load environment variables
load_dotenv()

app = typer.Typer()

@app.command()
def translate(
    text: str = typer.Argument(..., help="Text to be translated"),
    source: str = typer.Option(None, help="Source language (default: auto-detect)"),
    target: str = typer.Option("EN-US", help="Target language (default: EN-US)"),
    review: bool = typer.Option(False, "--review", "-r", help="Review and correct grammar (assumes English input)"),
):
    """
    Translate text using DeepL API.
    """
    # Check for review flag to perform grammar correction
    if review:
        try:
            tool = language_tool_python.LanguageTool('en-US')
            matches = tool.check(text)
            corrected_text = language_tool_python.utils.correct(text, matches)
            typer.echo(corrected_text)
            return
        except Exception as e:
            typer.echo(f"Grammar check failed: {e}", err=True)
            raise typer.Exit(code=1)

    api_key = os.getenv("DEEPL_API_KEY")
    if not api_key:
        typer.echo(
            "ERROR: Please set the DEEPL_API_KEY environment variable.", err=True
        )
        raise typer.Exit(code=1)

    try:
        translator = deepl.Translator(api_key)
        # source_lang is optional in deepl-python, if None it auto-detects
        result = translator.translate_text(
            text, source_lang=source, target_lang=target
        )
        typer.echo(result.text)

    except deepl.DeepLException as e:
        typer.echo(f"Translation failed: {e}", err=True)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
