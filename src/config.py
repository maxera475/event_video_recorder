# Video settings
# Change VIDEO_SOURCE from 0 to your video file's path
VIDEO_SOURCE = "output/sample_video.mp4" # <--- CHANGE THIS
FPS = 30.0 # Match this to your video's actual FPS if possible
FRAME_WIDTH = 1280 # Match your video's resolution
FRAME_HEIGHT = 720 # Match your video's resolution

# Event recording settings
BUFFER_SECONDS = 5 
POST_EVENT_SECONDS = 5

# Calculated values
BUFFER_SIZE = int(BUFFER_SECONDS * FPS)
POST_EVENT_FRAMES = int(POST_EVENT_SECONDS * FPS)

# Output settings
OUTPUT_DIR = "output"
METADATA_FILE = f"{OUTPUT_DIR}/metadata.json"