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
):
    """
    Translate text using DeepL API.
    """
    # Check for English source to perform grammar correction
    if source and source.upper() in ["EN", "EN-US", "EN-GB"]:
        try:
            tool = language_tool_python.LanguageTool('en-US')
            matches = tool.check(text)
            corrected_text = language_tool_python.utils.correct(text, matches)
            typer.echo(corrected_text)
            return
        except Exception as e:
            typer.echo(f"Grammar check failed: {e}", err=True)
            # Fallback to translation if grammar check fails? Or just exit?
            # For now, let's exit to be safe, or we could proceed to translation if user intended that.
            # But user request was specific about "review... and return corrections".
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
