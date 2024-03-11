# Llama Index RAG Application
A RAG implementation on Llama Index using Qdrant as storage.  Take some pdfs (you can either use the test pdfs include in /data or delete and use your own docs), index/embed them in a vdb, use LLM to inference and generate output.  Pretty nifty.

## How to use
- create local path and data subfolder 
- create virtual env using conda or however you choose
- install requirements.txt
- activate Ollama in terminal with "ollama run mistral" or whatever model you pick.  If you're using the new Ollama for Windows then not necessary since it runs in the background (ensure it's active).
- open llama_index_RAG.py and update lines 42 & 43 with your model of choice
- save and run the script
- observe results similar to:

![Image1](https://github.com/romilan24/llama-index-RAG/blob/main/RAG_inference_pdfs.JPG)
