from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper, DuckDuckGoSearchAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool
from datetime import datetime

# Tool 1: Wikipedia — for factual/science/history questions
wiki = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(
        top_k_results=2,
        doc_content_chars_max=1500
    )
)

# Tool 2: Web Search — only for current events and recent news
_search = DuckDuckGoSearchRun()

@tool
def search_web(query: str) -> str:
    """
    Searches the web for RECENT or CURRENT information only.
    Use this ONLY for: breaking news, today's events, latest updates, current prices.
    Do NOT use this for science, history, definitions or general knowledge — use Wikipedia instead.
    """
    try:
        return _search.run(query)
    except Exception:
        return "Web search unavailable right now. Try using Wikipedia instead."

# Tool 3: Current Date & Time
@tool
def get_current_datetime(query: str) -> str:
    """
    Returns the current date and time.
    Use this when the user asks what date it is, what time it is,
    or anything related to today's date.
    """
    return datetime.now().strftime("Date: %A, %d %B %Y | Time: %H:%M:%S")

# Tool 4: Calculator
@tool
def calculator(expression: str) -> str:
    """
    Evaluates a mathematical expression and returns the result.
    Use this for any arithmetic, percentage, or numerical calculations.
    Input must be a valid math expression like '15 * 4500 / 100'.
    """
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error in calculation: {str(e)}"

# Wikipedia first — agent reads tools in order
tools = [wiki, search_web, get_current_datetime, calculator]