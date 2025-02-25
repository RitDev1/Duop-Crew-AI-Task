from crewai import Agent, LLM
from textwrap import dedent
from langchain.llms import Ollama
from tools.search_tools import SearchTools
from langchain_openai import ChatOpenAI
from tools.calculator_tools import CalculatorTools
from tools.youtube_search import YouTubeSearchTools
from tools.financial_search_tool import CompanyValueTools
import os
""" 
Goal: Get a company name, search for its stock value, search for relevant videos on youtube and return a structured message to the user 
with the value and the videos, and some trivia about the company, relevant news, etc. 


Capitan: Financial manager
Workers: Financial search agent, Video search agent

"""




class CustomAgents:
    def __init__(self):
        self.Ollama  = LLM(model="ollama/llama3.1", base_url="http://localhost:11434")

    def financial_manager(self):
        return Agent(
            role="Financial Manager",
            backstory=dedent(f"""I'm an expert in financial analysis of comapanies and I can provide you with the value of a company, important information about the 
                             company, and relevant videos, also make recommendations about the company future, and i am able to write a message with these datas"""),
            goal=dedent(f"""Create a message that analyzes a company and creates a message with its stock value, total market value, important news about the company
            and relevant videos about the company, with the videos URLs and titles, and do a little analysis of the company future and recomandations"""),
            tools=[],
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama,
        )

    def financial_search_agent(self):
        return Agent(
            role="Financial Search Agent",
            backstory=dedent(f"""I am able to search for the stock value of a company, the total marketcap and other financial information, and search for relevant information about a company on the internet"""),
            goal=dedent(f"""Search for the precise stock value of a company and return it to the financial manager and Search for relevant information about a company and return it to the financial manager"""),
            tools=[SearchTools.search_internet,CompanyValueTools.get_company_value ],
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama,
        )

    def video_search_agent(self):
        return Agent(
            role="Video Search Agent",
            backstory=dedent(f"""I am able to search for relevant videos about a company on youtube"""),
            goal=dedent(f"""Search for relevant videos about a company on youtube and return them to the financial manager"""),
            tools=[YouTubeSearchTools.search_youtube],
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama,
        )




