import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

def get_client() -> Anthropic:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not set — copy .env.example to .env and fill it in")
    return Anthropic(api_key=api_key)
