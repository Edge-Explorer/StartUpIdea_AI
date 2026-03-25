from crewai import Task

class StartupValidationTasks:
    def market_research_task(self, agent, idea):
        return Task(
            description= f""" Analyze the market demand for this idea: '{idea}'. 
            Check for search trends, current user pain points, and overall market size. 
            Is the market growing or shrinking? """,
            expected_output= "A summary report of market trends, demand scores, and key target demographics.",
            agent= agent
        )
    
    def competitor_analysis_task(self, agent, idea):
        return Task(
            description=f"""Identify the top 3 direct competitors for: '{idea}'. 
            Analyze their pricing, features, and what users are complaining about in their reviews.""",
            expected_output="A SWOT analysis of the top 3 competitors and a list of 'market gaps' we can exploit.",
            agent=agent
        )
    
    def business_strategy_task(self, agent, idea):
        return Task(
            description=f"""Based on the market and competitor data for '{idea}', 
            suggest the best monetization model (SaaS, ads, etc.) and a 12-month scaling plan.""",
            expected_output="A detailed monetization strategy and a step-by-step roadmap for the first year.",
            agent=agent
        )

    def risk_analysis_task(self, agent, idea):
        return Task(
            description=f"""What are the biggest risks for '{idea}'? 
            Consider technical hurdles, legal issues, or potential shifts in the market.""",
            expected_output="A risk assessment report with 3-5 major risks and specific ways to mitigate each one.",
            agent=agent
        )
    
    def final_verdict_task(self, agent, idea, context):
        return Task(
            description=f"""Review all the specialist reports for the idea: '{idea}'. 
            Provide a final 'GO' or 'NO-GO' decision with a high-level executive summary.""",
            expected_output="A final verdict (YES/NO) followed by a 3-paragraph summary justifying the decision.",
            agent=agent,
            context=context # It lets the judge see the other reports!
        )