import os
import warnings
warnings.simplefilter("ignore", FutureWarning)
from crewai.tools import BaseTool
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.gemini import Gemini

class StartupDataRAGTool(BaseTool):
    name: str = "Startup Knowledge Base"
    description: str = "Search through local startup reports, business plans, and market data for deep insights."

    def _run(self, query: str) -> str:
        # 1. Check if the folder is empty
        if not os.path.exists("./data") or not os.listdir("./data"):
            return "The knowledge base is empty. Please add files to './data'."

        # 2. ⚡ Configure LlamaIndex to use Gemini (CRITICAL FIX)
        Settings.llm = Gemini(
            model="models/gemini-2.0-flash",
            api_key=os.getenv("GEMINI_API_KEY")
        )

        # 3. Load documents and Index
        documents = SimpleDirectoryReader("./data").load_data()
        index = VectorStoreIndex.from_documents(documents)
        
        # 4. Search and Respond
        query_engine = index.as_query_engine()
        response = query_engine.query(query)
        
        return str(response)