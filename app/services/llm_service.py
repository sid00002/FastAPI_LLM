class LLMService:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def chat(self, prompt: str) -> str:
        return f"Echo: {prompt}"
