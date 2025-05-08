"""Main application entry point."""

import argparse

from src.agent import run_prompt, extract_content


def main():
    """Run the main application."""
    parser = argparse.ArgumentParser(description="OpenAI agent for processing prompts")
    parser.add_argument("--prompt", "-p", type=str, help="The prompt to process")
    parser.add_argument("--model", "-m", type=str, default="gpt-4o", 
                      help="The model to use (default: gpt-4o)")
    
    args = parser.parse_args()
    
    if not args.prompt:
        args.prompt = input("Enter your prompt: ")
    
    print(f"\nProcessing prompt using {args.model}...")
    response = run_prompt(args.prompt, args.model)
    content = extract_content(response)
    
    print("\nResponse:")
    print(content)


if __name__ == "__main__":
    main()
