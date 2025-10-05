import datetime
import random

def simulate_event():
    """
    Simulates a detected event by generating a dictionary with metadata.
    GPS coordinates are randomized for demonstration. [cite: 13, 29]
    """
    return {
        "event_type": "manual_trigger", # Mock event type [cite: 11]
        "timestamp": datetime.datetime.now().isoformat(), # [cite: 12]
        "gps_coordinates": { # [cite: 13]
            "latitude": round(random.uniform(28.4, 28.8), 6),
            "longitude": round(random.uniform(77.0, 77.4), 6)
        }
    }