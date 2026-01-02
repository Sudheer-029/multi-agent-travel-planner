from google.adk.agents import Agent
from tools import search_transport

transport_agent = Agent(
    name="transport_agent",
    model="gemini-2.0-flash",
    description="Suggests transport options and comparisons.",
    instruction=(
        "Compare flights, trains, buses, and car options "
        "based on cost and duration."
    ),
    tools=[search_transport],
)
