import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class RiskAnalystAgent:
    def __init__(self):
        # 1. Initialize Gemini
        self.llm= ChatGoogleGenerativeAI(
            model= "gemini-2.0-flash",
            verbose= True,
            temperature= 0.3,
            google_api_key= os.getenv("GEMINI_API_KEY")
        )

    # 2. Define the Agent
    def get_agent(self) -> Agent:
        return Agent(
            role= "Risk Analyst",
            goal= "Identify potential risks and legal/tech challenges for the given startup idea.",
            backstory= """ You are an expert risk assessment specialist. You have a background 
            in law and technology, and you've seen many startups fail due to common pitfalls. 
            You excel at predicting failures and proposing mitigation strategies. """,
            llm= self.llm,
            verbose= True,
            allow_delegation= False
        )