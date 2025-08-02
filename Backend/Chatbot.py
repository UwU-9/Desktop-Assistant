
from langchain_ollama import OllamaLLM


def respond(prompt):
    model = OllamaLLM (model="deepseek-r1")

    result = model.invoke(prompt)

    print(result)