import os
from crewai.tools import BaseTool
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

class StartupDataRAGTool(BaseTool):
    # This is how the agent sees the tool
    name: str = "Startup Knowledge Base"
    description: str = "Search through local startup reports, business plans, and market data for deep insights."

    def _run(self, query: str) -> str:
        # 1. 📂 If the 'data' directory is empty, tell the agent!
        if not os.path.exists("./data") or not os.listdir("./data"):
            return "The knowledge base is currently empty. Please ask the user to add documents to the './data' folder."

        # 2. 🧠 Load the documents from the folder using LlamaIndex
        documents = SimpleDirectoryReader("./data").load_data()
        
        # 3. ⚡ Create a quick vector index
        index = VectorStoreIndex.from_documents(documents)
        
        # 4. 🔦 Search the data for the answer
        query_engine = index.as_query_engine()
        response = query_engine.query(query)
        
        return str(response)
