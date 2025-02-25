from langchain.tools import tool

class CalculatorTools():

    @tool ("Make a calculation")
    def calculate(operation):
        """Useful to perform any matehmatical operation, calculations, like sums, minus, multiplication
        division, etc.
        The imput to this tool should be a matematical operation, like 200*7, or 500/2*10 + 3.
        """
        try: 
            return eval(operation)
        except:
            return "Error: invalid syntax in mathematical expression"
