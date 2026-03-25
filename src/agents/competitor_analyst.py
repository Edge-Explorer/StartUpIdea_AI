import os
from crewai import Agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai_tools import TavilySearchTool

load_dotenv()

class CompetitorAnalystAgent:
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