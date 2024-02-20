# Llama Index RAG Application
A fine tuned RAG implementation on Llama Index using Quadrant as storage.  Take some pdfs, index/embed them in a vdb, use LLM to inference and generate output.  Pretty nifty.

## How to use
- create local path and data subfolder (you can either use the test pdfs or delete and use your own docs)
- create virtual env using conda or however you choose
- install requirements.txt
- activate Ollama in terminal with "ollama run mistral" or whatever model you pick.  If you're using the new Ollama for Windows then not necessary since it runs in the background (ensure it's active).
- open lang_RAG_pdf.py and update lines 42 & 43 with your model of choice
- save and run the script
- observe results similar to:

![Image1](https://github.com/romilan24/llama-index-RAG/blob/main/fine_tune_pdfs.JPG)
