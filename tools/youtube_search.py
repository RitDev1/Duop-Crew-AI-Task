from langchain.tools import tool
import requests 
import os


YOUTUBE_API_KEY = ""

class YouTubeSearchTools:
    
    @tool("Search YouTube")
    def search_youtube(query: str, max_results: int = 4) -> str:
        """
        Search for YouTube videos based on a query and return formatted results.
        
        Args:
            query: Search query string
            max_results: Number of results to return (default: 4)
            
        Returns:
            Formatted string with video information or error message
        """
        api_key = YOUTUBE_API_KEY
        if not api_key:
            return "Error: API key not configured (YOUTUBE_API_KEY)"
            
        url = "https://www.googleapis.com/youtube/v3/search"
        params = {
            'part': 'snippet',
            'q': query,
            'maxResults': max_results,
            'type': 'video',
            'key': api_key
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            if 'items' not in data or not data['items']:
                return "Nenhum vídeo encontrado para esta pesquisa."

            results = []
            for item in data['items']:
                video_id = item['id'].get('videoId', '')
                snippet = item.get('snippet', {})
                
                if not video_id:
                    continue
                    
                results.append('\n'.join([
                    f"Title: {snippet.get('title', 'Sem título')}",
                    f"Channel: {snippet.get('channelTitle', 'Canal desconhecido')}",
                    f"Link: https://www.youtube.com/watch?v={video_id}",
                    f"Published: {snippet.get('publishedAt', 'Data desconhecida')}",
                    f"Description: {snippet.get('description', 'Sem descrição')}",
                    "------------------"
                ]))

            return '\n'.join(results) if results else "Nenhum resultado relevante encontrado."

        except requests.exceptions.HTTPError as e:
            return f"YouTube API error: {str(e)}"
        except requests.exceptions.RequestException as e:
            return f"Conexion Error: {str(e)}"
