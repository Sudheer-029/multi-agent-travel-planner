def search_places(city: str) -> dict:
    return {
        "status": "success",
        "places": [
            "City Museum",
            "Hill View Point",
            "Old Fort",
            "Local Market"
        ]
    }


def search_hotels(city: str, budget: int) -> dict:
    return {
        "status": "success",
        "hotels": [
            {"name": "Hotel Vista", "price": 3000, "distance_km": 2, "rating": 4.5},
            {"name": "Budget Inn", "price": 1800, "distance_km": 4, "rating": 4.0},
            {"name": "Luxury Stay", "price": 6000, "distance_km": 1, "rating": 4.8},
        ]
    }


def search_transport(source: str, destination: str) -> dict:
    return {
        "status": "success",
        "options": [
            {"mode": "Flight", "cost": 5500, "duration_hr": 2},
            {"mode": "Train", "cost": 1200, "duration_hr": 10},
            {"mode": "Bus", "cost": 900, "duration_hr": 12},
            {"mode": "Car", "cost": 3500, "duration_hr": 9},
        ]
    }


def generate_itinerary(city: str, days: int) -> dict:
    return {
        "status": "success",
        "itinerary": {
            "Day 1": ["Local Market", "City Museum"],
            "Day 2": ["Hill View Point", "Old Fort"],
        }
    }
