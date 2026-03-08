import litellm
from app.core.config import settings

class GenAIService:
    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.model = model
        
        # Configure callbacks based on settings
        callbacks = []
        if settings.ENABLE_LANGSMITH:
            callbacks.append("langsmith")
        
        # Add OTEL if configured (OpenTelemetry integration can be complex,
        # here we just show how LiteLLM would use it)
        # callbacks.append("otel")
        
        litellm.success_callback = callbacks
        litellm.failure_callback = callbacks

    async def generate(self, prompt: str):
        """
        Generate a response from the LLM.
        """
        response = await litellm.acompletion(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    async def generate_structured(self, prompt: str, response_format: dict):
        """
        Generate a structured response from the LLM.
        """
        response = await litellm.acompletion(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            response_format=response_format
        )
        return response.choices[0].message.content
