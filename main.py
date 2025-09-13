from fastmcp import FastMCP
from langchain_community.utilities import SQLDatabase
from langchain_core.prompts import ChatPromptTemplate

mcp = FastMCP("SQL AGENT MCP")

db = SQLDatabase.from_uri("sqlite:///database.sqlite")

# SQL Agent Tools
# query_player_stats: Player performance analytics
# match_analysis: Match-level insights and comparisons
# team_performance: Team statistics and trends
# season_comparisons: Cross-season analysis
# head_to_head: Team vs team historical data
# Domain-Aware Query Processing
# Understand cricket terminology (strike rate, economy, etc.)
# Handle IPL-specific concepts (powerplay, death overs)
# Recognize player names, team names, and venues

# @mcp.tool
# def make_query(prompt: str) -> str:

#     table_info = db.get_table_info()
#     dialect = db.dialect
#     context = db.get_context()
#     top_k = 3

#     """Generate a SQL query to answer the question."""

#     system_message = f"""
#     Given an input question, create a syntactically correct {dialect} query to
#     run to help find the answer. Unless the user specifies in his question a
#     specific number of examples they wish to obtain, always limit your query to
#     at most {top_k} results. You can order the results by a relevant column to
#     return the most interesting examples in the database.

#     Limit the number of queries you make.

#     Pay attention to use only the column names that you can see in the schema
#     description. Be careful to not query for columns that do not exist. Also,
#     pay attention to which column is in which table.

#     Here is the relevant context from the database which has information about the 
#     relationships between tables and their columns:
#     {context}

#     Only use the following tables:
#     {table_info}
#     """

#     messages = ChatPromptTemplate.from_messages(
#         [
#             ("system", system_message),
#             ("user", f"Generate a query for : {prompt}"),
#         ]
#     ).format_messages(query=prompt)

#     return messages

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
    response = query.invoke(player_name=player_name)

    return response

@mcp.tool
def run_query(query: str) -> str:

    """Execute the SQL query and return the results."""

    result = db.run(query)
    return str(result)

if __name__ == "__main__":
    mcp.run()




