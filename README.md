# OpenAI Agent Project

A Python application that uses OpenAI's API to process prompts.

## Setup

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the package in development mode:
   ```
   pip install -e ".[dev]"
   ```
4. Copy the environment variables file and add your API key:
   ```
   cp .env.example .env
   ```
   Then edit the `.env` file with your actual OpenAI API key.

## Usage

Run the application with a prompt:
```
python -m src.main --prompt "Your prompt here"
```

Or run it interactively:
```
python -m src.main
```

## Testing

Run tests with pytest:
```
python -m pytest
```
