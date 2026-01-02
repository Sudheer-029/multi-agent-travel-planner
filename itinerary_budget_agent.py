from google.adk.agents import Agent
from tools import generate_itinerary

itinerary_budget_agent = Agent(
    name="itinerary_budget_agent",
    model="gemini-2.0-flash",
    description="Creates itinerary and estimates budget.",
    instruction=(
        "Prepare a day-wise itinerary and estimate overall travel budget."
    ),
    tools=[generate_itinerary],
)
