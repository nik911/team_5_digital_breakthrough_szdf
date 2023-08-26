from llama_cpp import Llama
llm = Llama(model_path="codellama-7b-instruct.ggmlv3.Q2_K.bin")
output = llm("Q: Name the planets in the solar system? A: ", max_tokens=32, stop=["Q:", "\n"], echo=True)
print(output)

