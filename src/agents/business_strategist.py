import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class BusinessStrategistAgent:
    def __init__(self):
        # 1. Initialize Gemini
        self.llm= ChatGoogleGenerativeAI(
            model= "gemini-2.0-flash",
            verbose= True,
            temperature= 0.7, # Higher creativity for strategy
            google_api_key= os.getenv("GEMINI_API_KEY")
        )

    # 2. Define the Agent
    def get_agent(self) -> Agent:
        return Agent(
            role= "Business Strategist",
            goal= "Develop a sustainable and scalable business model and monetization plan for the idea.",
            backstory= """ You are an expert business model innovator who has helped hundreds of 
            startups scale from zero to millions. You know everything about 
            SaaS, Freemium, and direct-to-consumer models. """,
            llm= self.llm,
            verbose= True,
            allow_delegation= False # Keeps the strategist focused on their own plan
        )    
