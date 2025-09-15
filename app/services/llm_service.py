import os
import httpx
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")
HF_MODEL = os.getenv("HF_MODEL", "gpt2")  # fallback to gpt2
API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"

HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}


async def generate_response(prompt: str) -> str:
    """
    Generate text using Hugging Face Inference API (async version)
    """
    try:
        payload = {"inputs": prompt}

        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(API_URL, headers=HEADERS, json=payload)
            response.raise_for_status()

        output = response.json()

        if isinstance(output, list) and "generated_text" in output[0]:
            return output[0]["generated_text"].strip()

        return str(output)
    except Exception as e:
        return f"Error: {str(e)}"
