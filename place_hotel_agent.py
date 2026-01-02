from google.adk.agents import Agent
from tools import search_places, search_hotels

place_hotel_agent = Agent(
    name="place_hotel_agent",
    model="gemini-2.0-flash",
    description="Finds places to visit and compares hotels.",
    instruction=(
        "Search best places to visit in a city and compare hotels "
        "based on budget, distance, and rating."
    ),
    tools=[search_places, search_hotels],
)
