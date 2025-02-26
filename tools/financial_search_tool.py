import os
import yfinance as yf
import requests
import json
from crewai import tool

SERPER_API_KEY = ""

class CompanyValueTools:
    
    @tool("Get Company Market Value")
    def get_company_value(company: str) -> str:
        """
        Get the current market value and financial information for a company.
        
        Args:
            company: Company name or stock ticker symbol (e.g.: 'Apple' or 'AAPL')
            
        Returns:
            Formatted string with company valuation details or error message
        """
        try:

            ticker = yf.Ticker(company)
            if not ticker.info or 'regularMarketPrice' not in ticker.info:
                return CompanyValueTools._search_company_symbol(company)
                
            return CompanyValueTools._format_company_data(ticker.info)
            
        except Exception as e:
            return f"Eror on finding the company value: {str(e)}"

    @staticmethod
    def _search_company_symbol(company_name: str) -> str:  # search for the ticker symbol
        api_key = SERPER_API_KEY
        if not api_key:
            return "Error: API key not configured: (SERPER_API_KEY)"
            
        url = "https://google.serper.dev/search"
        payload = json.dumps({
            "q": f"{company_name} stock ticker symbol",
            "gl": "us",
            "hl": "en"
        })
        
        headers = {
            'X-API-KEY': api_key,
            'Content-Type': 'application/json'
        }
        
        try:
            response = requests.post(url, headers=headers, data=payload)
            response.raise_for_status()
            data = response.json()
            if 'knowledgeGraph' in data:
                symbol = data['knowledgeGraph'].get('title', '').split(':')[-1].strip()
                if symbol:
                    ticker = yf.Ticker(symbol)
                    if ticker.info:
                        return CompanyValueTools._format_company_data(ticker.info)
            
            return f"Not able to find information about the company: {company_name}"
            
        except Exception as e:
            return f"Error on finding the symbol: {str(e)}"

    @staticmethod
    def _format_company_data(info: dict) -> str:
        return '\n'.join([
            f"Empresa: {info.get('longName', 'N/A')}",
            f"Símbolo: {info.get('symbol', 'N/A')}",
            f"Valor de Mercado: {info.get('marketCap', 'N/A'):,} USD",
            f"Preço Atual: {info.get('regularMarketPrice', 'N/A')} USD",
            f"Setor: {info.get('sector', 'N/A')}",
            f"Indústria: {info.get('industry', 'N/A')}",
            "------------------"
        ])
