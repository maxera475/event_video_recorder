# Video settings
VIDEO_SOURCE = 0  # 0 for the default webcam
FPS = 20.0        # Assumed frames per second for the camera
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Event recording settings
BUFFER_SECONDS = 15 # Pre-event buffer duration in seconds
POST_EVENT_SECONDS = 15 # Post-event recording duration

# Calculated values
BUFFER_SIZE = int(BUFFER_SECONDS * FPS)
POST_EVENT_FRAMES = int(POST_EVENT_SECONDS * FPS)

# Output settings
OUTPUT_DIR = "output"
METADATA_FILE = f"{OUTPUT_DIR}/metadata.json"