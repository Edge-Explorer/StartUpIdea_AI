import os
from dotenv import load_dotenv
from crewai import Crew, Process

from agents.market_researcher import MarketResearcherAgent
from agents.competitor_analyst import CompetitorAnalystAgent
from agents.business_strategist import BusinessStrategistAgent
from agents.risk_analyst import RiskAnalystAgent
from agents.final_decision import FinalDecisionAgent

from tasks import StartupValidationTasks

load_dotenv()

def run_crew():
    # The startup idea (Change this later to test!)
    idea= "I want to build an AI fitness app for busy professionals"

    # 1. Initialize all the agents
    market_agent = MarketResearcherAgent().get_agent()
    competitor_agent = CompetitorAnalystAgent().get_agent()
    strategist_agent = BusinessStrategistAgent().get_agent()
    risk_agent = RiskAnalystAgent().get_agent()
    decision_agent = FinalDecisionAgent().get_agent()

    # 2. Initialize the tasks
    tasks= StartupValidationTasks()

    t1 = tasks.market_research_task(market_agent, idea)
    t2 = tasks.competitor_analysis_task(competitor_agent, idea)
    t3 = tasks.business_strategy_task(strategist_agent, idea)
    t4 = tasks.risk_analysis_task(risk_agent, idea)

    # Passing the results of t1-t4 as context for the judge
    t5 = tasks.final_verdict_task(decision_agent, idea, [t1, t2, t3, t4])

    # 3. Create the Crew and define the process
    crew= Crew(
        agents= [market_agent, competitor_agent, strategist_agent, risk_agent, decision_agent],
        tasks= [t1, t2, t3, t4, t5],
        process= Process.sequential,
        verbose= True
    )

    # 4. Run the Crew
    print(f"\n\n--- Starting the Startup Idea Validator for: '{idea}' ---\n")
    result= crew.kickoff()

    print("\n\n########################")
    print("##   FINAL REPORT     ##")
    print("########################\n")
    print(result)

if __name__ == "__main__":
    run_crew()