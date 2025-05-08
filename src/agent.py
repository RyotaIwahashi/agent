"""OpenAI Agent implementation."""

import os
from typing import Dict, Any

import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def run_prompt(prompt: str, model: str = "gpt-4o") -> Dict[str, Any]:
    """Run a prompt through the OpenAI API.

    Args:
        prompt: The user prompt to process
        model: The model to use (defaults to gpt-4o)

    Returns:
        The API response as a dictionary
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response


def extract_content(response: Dict[str, Any]) -> str:
    """Extract the content from an OpenAI API response.
    
    Args:
        response: The OpenAI API response
        
    Returns:
        The extracted content as a string
    """
    return response.choices[0].message.content
