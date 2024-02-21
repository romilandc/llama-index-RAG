from llama_index.llms.ollama import Ollama
from llama_index.core import VectorStoreIndex, ServiceContext, SimpleDirectoryReader
from qdrant_client import QdrantClient
from llama_index.core import StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core.callbacks import CallbackManager

### Monitoring Setup ###
import phoenix as px

# Start Phoenix server
session = px.launch_app()

from phoenix.trace.llama_index import (
    OpenInferenceTraceCallbackHandler,
)

# Initialize the callback handler for tracing
callback_handler = OpenInferenceTraceCallbackHandler()

# Load data
reader = SimpleDirectoryReader(input_dir="./data")
documents = reader.load_data()

# Initialize QdrantClient and QdrantVectorStore
qdrant_client = QdrantClient(":memory:") # QdrantClient(path="./qdrant_data")

qdrant_vector_store = QdrantVectorStore(
    qdrant_client=qdrant_client, 
    collection_name="zarathustra",
    client = qdrant_client
)

qdrant_storage_context = StorageContext.from_defaults(
    vector_store=qdrant_vector_store
)

# Initialize Ollama and ServiceContext
print("Initializing Ollama...")
'''
llm = Ollama(
    model="mistral",
    base_url="http://localhost:11434",
    request_timeout=100
)
'''
llm = Ollama(
    model="mistral",
    request_timeout=100
)

service_context = ServiceContext.from_defaults(
    llm=llm, 
    embed_model="local",
    callback_manager=CallbackManager(handlers=[callback_handler]),
)

# Create VectorStoreIndex and query engine
print("Creating index...")
qdrant_index = VectorStoreIndex.from_documents(
    documents, storage_context=qdrant_storage_context, service_context=service_context
)

print("Creating query engine...")
query_engine = qdrant_index.as_query_engine()

# Perform a query and print the response
print("Querying...")

# Create a python chat which takes users input and returns a response in a loop
print("Starting chat...")
while True:
    user_input = input("You: ")
    # If the user types "exit", exit the loop
    if user_input == "exit":
        break
    response = query_engine.query(user_input)
    print(response)

px.active_session().url