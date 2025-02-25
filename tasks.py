from crewai import Task
from textwrap import dedent
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def search_company_value(self, agent, company_name):
        return Task(
            description=dedent(
                f"""
            **Task**: Search for a company stock value and marketcap. 
            **Description**: Search on the internet for the stock EXACT value of the company on a given time, and also search and summarize recent news articles, press
    releases, and market analyses related to the stock and its industry.
    Pay special attention to any significant events, market sentiments, and analysts' opinions. 
    Also include upcoming events like earnings and others.
            
            {self.__tip_section()}
    
            Make sure to use the most recent data as possible.
            **Parameters**:
            The company name is: {company_name}
            
        """
            ),
            expected_output="""A report that includes a comprehensive summary of the latest news, 
    any notable shifts in market sentiment, and potential impacts on the stock. Also make sure to return the stock ticker as {company_stock}.
    Make sure to use the most recent data as possible, and very cleary the current stock value of the company and its total value.""", 
            agent=agent,
        )

    def search_videos(self, agent, company_name):
         return Task(
            description=dedent(
                f"""
            **Task**: Search for videos on youtube related to the company. 
            **Description**: Search on youtube for videos related to the company and its latest news and important information make a brief summary of the videos topic. .
            
            {self.__tip_section()}
    
            Make sure to use the most recent data as possible.
            **Parameters**:
            The company name is: {company_name}
            
        """
            ),
            expected_output="""The URLs and titles of the videos found on youtube related to the company, and a brief summary of the videos topic.""", 
            agent=agent,
        )
    def formulate_response(self, agent, company_name):
            return Task(
                description=dedent(
                    f"""
                **Task**: Formulate a response for the user. 
                **Description**: Compile an answer for the user, in Brazilian Portuguese, with the urls of the videos found, the title of the videos and a brief summary,
                 the relevant information about the company and its stock value. Make the answer in a consise way, like you were writing a message .
                
                {self.__tip_section()}
                **Parameters**:
                The company name is: {company_name}
                
            """
                ),
                expected_output="""A consise answer in Brazilian Portuguese with the urls of the videos found, the title of the videos and a brief summary,
                 the relevant information about the company and its stock value. Make the answer in a consise way, like you were writing a message .""", 
                agent=agent,
            )