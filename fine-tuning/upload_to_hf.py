from langchain_community.llms import LlamaCpp

# Initialize a pipeline-style object for GGUF
llm = LlamaCpp(
    model_path="./my_model/gemma-3-4b-it.Q4_K_M.gguf",
    temperature=0.7,
    max_tokens=256,
    n_ctx=2048,
    verbose=False
)

# Run inference
response = llm.invoke("Summarize the text here...")
print(response)