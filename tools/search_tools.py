import json
import requests
from langchain.tools import tool
import os

SERPER_API_KEY = "d069c7a4920d384e5cca9a0ee0c6608890776115"

class SearchTools:

    @tool("Search the internet")
    def search_internet(query):
        """Useful to search the internet about a given topic and return relevant results."""
        top_result_to_return = 4
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': SERPER_API_KEY,
            'content-type': 'application/json'
        }

        try:
            response = requests.post(url, headers=headers, data=payload)
            response.raise_for_status() 

            data = response.json()
            if 'organic' not in data:
                return "Sorry, I couldn't find anything about that. There might be an issue with your Serper API key or the query."

            results = data['organic']
            string = []
            for result in results[:top_result_to_return]:
                try:
                    string.append('\n'.join([
                        f"Title: {result['title']}",
                        f"Link: {result['link']}",
                        f"Snippet: {result['snippet']}",
                        "\n-----------------"
                    ]))
                except KeyError:
                    continue  

            return '\n'.join(string) if string else "No relevant results found."

        except requests.exceptions.RequestException as e:
            return f"An error occurred while making the request: {str(e)}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"