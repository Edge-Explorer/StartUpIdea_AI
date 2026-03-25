from crewai import Agent, LLM
import os
from dotenv import load_dotenv
from crewai_tools import TavilySearchTool

load_dotenv()

class MarketResearcherAgent:
    def __init__(self):
        # 1. Initialize the Search Tool
        self.search_tool= TavilySearchTool(api_key=os.getenv("TAVILY_API_KEY"))

        # 2. Use CrewAI's native LLM wrapper for Gemini 2.0
        self.llm = LLM(
            model="gemini/gemini-2.0-flash",
            temperature=0.5,
            api_key=os.getenv("GEMINI_API_KEY")
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