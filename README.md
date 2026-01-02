# 🧭 Multi-Agent Travel Planner (Google ADK + Gemini)

A **multi-agent travel planning system** built using **Google Agent Development Kit (ADK)** and **Gemini models**.  
The system uses **agent orchestration** to plan trips end-to-end — from destinations and hotels to transport, itinerary, and budget.

This project demonstrates **agentic AI design patterns** suitable for real-world applications and interviews.

---

## 🚀 Features

- 🏙️ Discover places to visit
- 🏨 Search & compare hotels (budget, distance, rating)
- 🚆 Compare transport options (flight, train, bus, car)
- 🗓️ Generate day-wise itinerary
- 💰 Estimate overall travel budget
- 🤖 True **multi-agent orchestration** using ADK

---

## 🧠 Architecture Overview

User Query
│
▼
Root Travel Planner Agent
├── Place & Hotel Agent
├── Transport Agent
└── Itinerary & Budget Agent


Each agent is **domain-specialized** and coordinated by a root agent.

---

## 🤖 Agents

### 1️⃣ Place & Hotel Agent
- Finds popular tourist places
- Searches hotels
- Compares hotels by:
  - Price
  - Distance
  - Ratings

### 2️⃣ Transport Agent
- Suggests:
  - Flights
  - Trains
  - Buses
  - Car / Bike
- Compares cost and travel duration

### 3️⃣ Itinerary & Budget Agent
- Creates day-wise travel plan
- Estimates approximate trip budget

### 4️⃣ Root Travel Planner Agent
- Orchestrates all sub-agents
- Merges results into a single response
- Acts as the user-facing agent

---

## 📁 Project Structure

multi-agent-travel-planner/
├── tools.py
├── place_hotel_agent.py
├── transport_agent.py
├── itinerary_budget_agent.py
├── root_agent.py
└── README.md


---

## 🛠️ Tools (Mocked)

The project currently uses mock tools that can later be replaced with real APIs.

- `search_places`
- `search_hotels`
- `search_transport`
- `generate_itinerary`

---

## 🧩 Tech Stack

- Python 3.10+
- Google Agent Development Kit (ADK)
- Gemini 2.0 Flash
- Agentic AI patterns

---

## ▶️ How to Run

### 1️⃣ Install dependencies
```bash
pip install google-adk

2️⃣ Configure Gemini / Google AI credentials

Ensure your environment is set up with valid Google AI access.

Run the root agent
from root_agent import travel_planner_agent

Provide a user query to receive a complete travel plan.

🧪 Example Use Case

Input:
Plan a 3-day trip to Jaipur with a budget of ₹15,000
Output

Places to visit

Hotel comparison

Transport options

Day-wise itinerary

Estimated total budget

🔮 Future Enhancements

Integrate real APIs:

Google Places

Booking.com / Agoda

Skyscanner / Amadeus

Add memory for user preferences

Add weather and visa agents

Deploy as:

REST API

Web app

Chat UI

🧠 Key Concepts Demonstrated

Multi-agent orchestration

Tool-augmented LLMs

Modular agent design

Scalable agent architecture

Real-world agentic workflows

📄 License

This project is for learning and demonstration purposes.
Feel free to fork and extend.
