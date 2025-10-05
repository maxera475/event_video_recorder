import json
from src import config

def view_recorded_events():
    """
    Reads the metadata file and prints a summary of each recorded event.
    """
    try:
        with open(config.METADATA_FILE, 'r') as f:
            events = json.load(f)

        if not events:
            print("No events have been recorded yet.")
            return

        print("--- Recorded Events ---")
        for i, event in enumerate(events, 1):
            print(f"\nEvent #{i}:")
            print(f"  - Filename:    {event.get('filename', 'N/A')}")
            print(f"  - Timestamp:   {event.get('timestamp', 'N/A')}")
            print(f"  - Event Type:  {event.get('event_type', 'N/A')}")
            gps = event.get('gps_coordinates', {})
            print(f"  - GPS:         Lat {gps.get('latitude', 'N/A')}, Lon {gps.get('longitude', 'N/A')}")
        print("\n-----------------------")

    except FileNotFoundError:
        print(f"Metadata file not found. Have you recorded any events yet?")
        print(f"Expected location: {config.METADATA_FILE}")
    except json.JSONDecodeError:
        print("Error: Could not parse the metadata file. It might be empty or corrupted.")

if __name__ == "__main__":
    view_recorded_events()