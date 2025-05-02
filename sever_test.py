from langchain_community.llms import Ollama

llm = Ollama(model="llama2", base_url="http://localhost:11434/")
llm.invoke("Why is the sky blue?")