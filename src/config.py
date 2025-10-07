VIDEO_SOURCE = "output/sample_video.mp4"
FPS = 30.0 
FRAME_WIDTH = 1280 
FRAME_HEIGHT = 720 

# Event recording settings
BUFFER_SECONDS = 5 
POST_EVENT_SECONDS = 5

# Calculated values
BUFFER_SIZE = int(BUFFER_SECONDS * FPS)
POST_EVENT_FRAMES = int(POST_EVENT_SECONDS * FPS)

# Output settings
OUTPUT_DIR = "output"
METADATA_FILE = f"{OUTPUT_DIR}/metadata.json"