import os
import yfinance as yf
import requests
import json
from langchain.tools import tool

class CompanyValueTools:
    
    @tool("Get Company Market Value")
    def get_company_value(company):
        """
        Get the current market value and financial information for a company and its stock value.
        
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
            return f"Errof on finding the company value: {str(e)}"
    def _format_company_data(info: dict) -> str:
        return '\n'.join([
            f"Empresa: {info.get('longName', 'N/A')}",
            f"Valor de Mercado: {info.get('marketCap', 'N/A'):,} USD",
            f"Preço Atual: {info.get('regularMarketPrice', 'N/A')} USD",
            f"Setor: {info.get('sector', 'N/A')}",
            f"Indústria: {info.get('industry', 'N/A')}",
            "------------------"
        ])