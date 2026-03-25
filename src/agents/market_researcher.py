from crewai_tools import TavilySearchTool
import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class MarketResearcherAgent:
    def __init__(self):
        # 1. Initialize the Search Tool
        self.search_tool= TavilySearchTool()

        # 2. Initialize Gemini
        self.llm= ChatGoogleGenerativeAI(
            model= "gemini-2.0-flash",
            verbose= True,
            temperature= 0.5,
            google_api_key= os.getenv("GEMINI_API_KEY")
        )

    # 3. Define the Agent
    def get_agent(self) -> Agent:

        return Agent(
            role= "Market Research Specialist",
            goal= 'Analyze market demand, user pain points, and current trends for the given startup idea.',
            backstory= """ You are an expert market analyst with a background in venture capital. 
            You have a "nose" for identifying which ideas are just hype and which have real 
            long-term potential. You focus on data, search trends, and demographic shifts. """,
            tools= [self.search_tool],
            llm= self.llm,
            verbose= True,
            allow_delegation= False
        )