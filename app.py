from langchain import LlamaCpp
from langchain import PromptTemplate

llm = LlamaCpp(model_path="/Users/nishchaysinha/llamaDocumentConvo/models/llama-2-7b.ggmlv3.q4_0.bin")
template = """Q: Who directed {movie_name}

Answer:"""

prompt = PromptTemplate.from_template(template)

prompt.input_variables
prompt.template

formatted_prompt = prompt.format_prompt(movie_name="The Matrix")
print(formatted_prompt)

print(llm(prompt=formatted_prompt, llm=llm, stop=["Q:", "/n"]))
