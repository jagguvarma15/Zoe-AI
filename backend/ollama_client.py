from langchain.llms.ollama import Ollama

def get_lora_model(model_name: str = "llama2"):
    """
    Connect to the base LLaMA2 model served by Ollama.
    """
    return Ollama(model=model_name)
