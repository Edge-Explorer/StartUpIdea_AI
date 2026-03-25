import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class FinalDecisionAgent:
    def __init__(self):
        # 1. Initialize Gemini
        self.llm= ChatGoogleGenerativeAI(
            model= "gemini-2.0-flash",
            verbose= True,
            temperature= 0.2,
            google_api_key= os.getenv("GEMINI_API_KEY")
        )
    
    def get_agent(self) -> Agent:
        return Agent(
            role= "Final Decision Expert",
            goal= "Combine all reports and provide a final verdict on the viability of the startup idea.",
            backstory= """ You are a world-class strategic decision-maker. You take 
            objective data from other specialists and turn it into a final 
            recommendation. You are known for being blunt, honest, and decisive. """,
            llm= self.llm,
            verbose= True,
            allow_delegation= False
        )