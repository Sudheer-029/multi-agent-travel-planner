from google.adk.agents import Agent
from place_hotel_agent import place_hotel_agent
from transport_agent import transport_agent
from itinerary_budget_agent import itinerary_budget_agent

travel_planner_agent = Agent(
    name="travel_planner_agent",
    model="gemini-2.0-flash",
    description="End-to-end travel planning agent.",
    instruction=(
        "You are a smart travel planner. "
        "Delegate tasks to specialized agents and merge results into "
        "a complete travel plan with hotels, transport, itinerary, and budget."
    ),
    sub_agents=[
        place_hotel_agent,
        transport_agent,
        itinerary_budget_agent
    ],
)
