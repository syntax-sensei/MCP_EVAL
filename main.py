from fastmcp import FastMCP
from langchain_community.utilities import SQLDatabase
from langchain_core.prompts import ChatPromptTemplate

mcp = FastMCP("SQL AGENT MCP")

db = SQLDatabase.from_uri("sqlite:///database.sqlite")

@mcp.tool
def query_player_stats(player_name: str) -> str:

    """Generate a SQL query to fetch player statistics."""

    table_info = db.get_table_info()
    context = db.get_context()
    dialect = db.dialect
    top_k = 3

    system_message = f"""
    Given an input question, create a syntactically correct {dialect} query to run to help find the player_stats of {player_name} from various tables. 
    Understand cricket terminology (strike rate, economy, etc.) and relationships between tables and their columns using {context}.
    Only use the following tables: {table_info}
    """

    query = ChatPromptTemplate(
    [
        ("system", system_message), 
        ("user", f"Generate a query to Fetch player statistics for {player_name}")
    ]
    )

    return query

@mcp.tool
def match_analysis(match_id: int) -> str:
    
    """Generate a SQL query to analyze a specific match."""

    table_info = db.get_table_info()
    context = db.get_context()
    dialect = db.dialect
    top_k = 3

    system_message = f"""
    Given an input question, create a syntactically correct {dialect} query to run to help find the match_analysis of match_id {match_id} from various tables. 
    Understand cricket terminology (strike rate, economy, etc.) and relationships between tables and their columns using {context}.
    Only use the following tables: {table_info}
    """

    query = ChatPromptTemplate(
    [
        ("system", system_message), 
        ("user", f"Generate a query to Analyze match with ID {match_id}")
    ]
    )

    return query

@mcp.tool
def team_performance(team_name: str) -> str:

    """Generate a SQL query to evaluate team performance."""

    table_info = db.get_table_info()
    context = db.get_context()
    dialect = db.dialect
    top_k = 3

    system_message = f"""
    Given an input question, create a syntactically correct {dialect} query to run to help find the team_performance of {team_name} from various tables. 
    Understand cricket terminology (strike rate, economy, etc.) and relationships between tables and their columns using {context}.
    Only use the following tables: {table_info}
    """

    query = ChatPromptTemplate(
    [
        ("system", system_message), 
        ("user", f"Generate a query to Evaluate team performance for {team_name}")
    ]
    )

    return query


@mcp.tool
def season_comparisons(season_year: int) -> str:

    """Generate a SQL query to compare seasons."""

    table_info = db.get_table_info()
    context = db.get_context()
    dialect = db.dialect
    top_k = 3

    system_message = f"""
    Given an input question, create a syntactically correct {dialect} query to run to help find the season_comparisons of season_year {season_year} from various tables. 
    Understand cricket terminology (strike rate, economy, etc.) and relationships between tables and their columns using {context}.
    Only use the following tables: {table_info}
    """

    query = ChatPromptTemplate(
    [
        ("system", system_message), 
        ("user", f"Generate a query to Compare seasons for the year {season_year}")
    ]
    )

    return query

@mcp.tool
def head_to_head(team1: str, team2: str) -> str:

    """Generate a SQL query to analyze head-to-head statistics."""

    table_info = db.get_table_info()
    context = db.get_context()
    dialect = db.dialect
    top_k = 3

    system_message = f"""
    Given an input question, create a syntactically correct {dialect} query to run to help find the head_to_head statistics between {team1} and {team2} from various tables. 
    Understand cricket terminology (strike rate, economy, etc.) and relationships between tables and their columns using {context}.
    Only use the following tables: {table_info}
    """

    query = ChatPromptTemplate(
    [
        ("system", system_message), 
        ("user", f"Generate a query to Analyze head-to-head statistics between {team1} and {team2}")
    ]
    )

    return query

@mcp.tool
def run_query(query: str) -> str:

    """Execute the SQL query and return the results."""

    result = db.run(query)
    return str(result)

if __name__ == "__main__":
    mcp.run()




