import os
from crewai import Crew
from agents import CustomAgents
from tasks import CustomTasks
from dotenv import load_dotenv
load_dotenv()

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class CustomCrew:
    def __init__(self, company_name):
        self.company_name = company_name

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        financial_manager = agents.financial_manager()  
        video_search_agent = agents.video_search_agent()
        financial_search_agent = agents.financial_search_agent()
        

        # Custom tasks include agent name and variables as input
        search_company_value= tasks.search_company_value(
            financial_search_agent,
            self.company_name,
        )

        search_videos = tasks.search_videos(
            video_search_agent,
            self.company_name
        )
        formulate_message = tasks.formulate_response(
            financial_manager,
            self.company_name
        )


        # Define your custom crew here
        crew = Crew(
            agents=[financial_manager, video_search_agent, financial_search_agent],
            tasks=[search_company_value, search_videos, formulate_message],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Bem vindo ao programa de pesquisa de dados de empresas")
    print("-------------------------------")
    company_name = input("Digite o nome da empresa que deseja pesquisar: ")
    print("-------------------------------")


    custom_crew = CustomCrew(company_name=company_name)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
