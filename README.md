## IPL Analytics MCP Server

This is an MCP (Model Context Protocol) server that provides intelligent SQL querying capabilities for the Indian Premier League (IPL) database, enabling natural language queries to be converted into SQL and executed against a comprehensive cricket analytics database.

## Key Database Entities

Based on the schema diagram, the database contains:

Core Match Data:

- Match details (venue, date, teams, outcomes)
- Ball-by-ball data with detailed events
- Toss decisions and match results

Player Information:

- Comprehensive player profiles (DOB, batting/bowling styles)
- Performance statistics and career data
- Team affiliations and roles
- Geographic & Venue Data:

City and country information

- Venue details and match locations

Game Mechanics:

- Wicket types and dismissal methods
- Batting and bowling styles
- Umpire and official information

## Capabilities:

- Natural Language to SQL Translation
- Convert cricket-specific queries into optimized SQL
- Handle complex aggregations and multi-table joins

SQL Agent Tools

- `query_player_stats`: Player performance analytics
- `match_analysis`: Match-level insights and comparisons
- `team_performance`: Team statistics and trends
- `season_comparisons`: Cross-season analysis
- `head_to_head`: Team vs team historical data

Domain-Aware Query Processing
- Understand cricket terminology (strike rate, economy, etc.)
- Handle IPL-specific concepts (powerplay, death overs)
- Recognize player names, team names, and venues