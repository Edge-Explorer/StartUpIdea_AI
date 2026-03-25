import os
from dotenv import load_dotenv
from crewai import Agent, LLM

load_dotenv()

class FinalDecisionAgent:
    def __init__(self):
        # Use CrewAI's native LLM wrapper for Gemini 2.0
        self.llm = LLM(
            model="gemini/gemini-2.0-flash",
            temperature=0.2, # Very stable for decisions
            api_key=os.getenv("GEMINI_API_KEY")
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