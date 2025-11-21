# deepl-translator-cli# deepl-translator

A simple command-line interface (CLI) tool to translate text using the DeepL API.

## Features

- Translate text directly from the command line
- Default translation from Brazilian Portuguese (`PT-BR`) to American English (`EN-US`)
- Override source and target languages with command options
- **Grammar Correction**: Automatically correct English grammar when source is set to `EN`, `EN-US`, or `EN-GB`

## Requirements

- Python 3.7+
- DeepL Python SDK (`deepl`)
- Typer for CLI interface

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/deepl-translator-cli.git
    cd deepl-translator-cli
    ```

2. Install with Poetry:

    ```bash
    poetry install
    ```

3. Set your DeepL API key:

    ```bash
    export DEEPL_API_KEY="your-api-key-here"
    ```

## Usage

Translate text with default languages (auto-detect to EN-US):

```bash
poetry run deepl-cli "Olá, mundo"
```

Override languages:

```bash
poetry run deepl-cli "bonjour" --source FR --target EN-GB
```

### Grammar Correction

Use the `-r` or `--review` flag to perform grammar correction (assumes English input):

```bash
poetry run deepl-cli "I has a apple" -r
# Output: I have an apple
```

## Building the Package

To build the package for distribution (PyPI):

```bash
poetry build
```

This will create `.tar.gz` and `.whl` files in the `dist/` directory.

You can then install it via pip:

```bash
pip install dist/deepl_translator_cli-0.1.7-py3-none-any.whl
```
