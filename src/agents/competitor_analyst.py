import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from crewai_tools import TavilySearchTool

load_dotenv()

class CompetitorAnalystAgent:
    def __init__(self):
        # 1. Initialize the Search Tool
        self.search_tool= TavilySearchTool(api_key=os.getenv("TAVILY_API_KEY"))

        # 2. Use CrewAI's native LLM wrapper for Gemini 2.0
        self.llm = LLM(
            model="gemini/gemini-2.0-flash",
            temperature=0.3, # lower for facts
            api_key=os.getenv("GEMINI_API_KEY")
        )

    # 3. Define the Agent
    def get_agent(self) -> Agent:
        return Agent(
            role= 'Competitor Analyst',
            goal= 'Identify and analyze direct and indirect competitors in the space. Find their strengths and weaknesses.',
            backstory="""You are a competitive intelligence expert. You excel at finding 
            real-world brands, analyzing their pricing, and detecting the "gaps" 
            they are leaving open for new startups.""",
            
            tools= [self.search_tool],
            llm= self.llm,
            verbose= True,
            allow_delegation= False
        )