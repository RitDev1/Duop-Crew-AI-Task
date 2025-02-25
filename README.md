This project uses the CrewAI framework to automate financial research on publicly traded companies. The system collects, analyzes, and summarizes key financial metrics (revenue, profit, debt, market trends) using specialized AI agents. It generates structured reports in JSON/PDF formats and supports customization for specific companies or sectors.

- Technologies
  CrewAI: Framework for orchestrating collaborative AI agent teams.
  
  LangChain: NLP integration for data processing.
  
  Serper API: Real-time search engine for data collection.
  
  Ollama: Local server to run LLMs.
  
  Llama3.2: Open-source LLM made by Meta.
  
  Python: Core programming language.

The framework is based on creating AI agents, tasks for them to run, and tools for them to use to complete the tasks. 

-Agents created: 
  Financial Researcher:

  Collects raw data from public sources (e.g., Google Finance, SEC filings).

  Uses Serper API for real-time web searches.

  Financial Manager:

  Analyzes the information provided and write the message to the user

  Video Resarcher:

  Searches for videos related to the company

- Tasks Created: 

  Financial search task: task that uses the yaahoo finance to provide the real time stock value of a company, as well as other financial info.

  Youtube search task: task that searches for relevant videos on youtube

  Message write task: task that creates a message for the user

- Custom tools created: 

  Financial search tool: tool that uses yfinance to pull from the yahoo finance the real time financial data of the company 

  Youtube search tool: tool that uses the youtube API to search for relevant videos about the company

  Search tool: tool that searches on google for relevant info about the company, using Serper's API

- Requirements:
  Are required the libraries present on requiriments.txt
  
  On cmd type "pip install requirements.txt" to install the requirements. 
  
  Youtube Data V3 API key and Serper API key are required
  
  You need to have Ollama installed on your computer and also have ollama local server running when trying to run the program (type ollama serve, if the ollama local server is not running yet)
  
  You need to have Llama3.1 installed on your computer, type on the terminal "ollama pull llama3.1" to install it. You can switch the llm you are running by swapping the model, on agents.py line 25. 

- Usage

  Run the main program. It will ask you for the company name. Type it and wait for the agents to process the information. The crew will output a message in Brazilian Portuguese with the data it searched. 
  

