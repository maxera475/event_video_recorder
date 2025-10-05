import cv2
import json
import os
import threading
from datetime import datetime
from typing import List, Dict, Any
import numpy as np

from src import config

def save_metadata(event_data: Dict[str, Any]):
    """
    Appends event metadata to the central JSON file.
    Creates the file if it doesn't exist. [cite: 28]
    """
    if not os.path.exists(config.METADATA_FILE):
        with open(config.METADATA_FILE, 'w') as f:
            json.dump([], f)

    with open(config.METADATA_FILE, 'r+') as f:
        metadata_list = json.load(f)
        metadata_list.append(event_data)
        f.seek(0)
        json.dump(metadata_list, f, indent=4)


def _save_clip_thread(
    pre_event_buffer: List[np.ndarray],
    video_capture: cv2.VideoCapture,
    event_data: Dict[str, Any]
):
    """
    Thread target function to record post-event frames and save the full clip.
    This prevents the main loop from freezing during I/O operations.
    """
    print(f"[{datetime.now()}] Event detected! Starting to save clip...")

    # 1. Generate a unique filename for the video clip
    timestamp_str = datetime.fromisoformat(event_data["timestamp"]).strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp_str}_{event_data['event_type']}.mp4"
    filepath = os.path.join(config.OUTPUT_DIR, filename)
    event_data["filename"] = filename # Add filename to metadata

    # 2. Record the post-event frames
    post_event_frames = []
    for _ in range(config.POST_EVENT_FRAMES):
        ret, frame = video_capture.read()
        if not ret:
            break
        post_event_frames.append(frame)
        # Add a small delay to approximate real-time FPS
        cv2.waitKey(int(1000 / config.FPS))

    # 3. Combine pre-buffer and post-event frames
    full_clip_frames = pre_event_buffer + post_event_frames

    # 4. Write the video file
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(filepath, fourcc, config.FPS, (config.FRAME_WIDTH, config.FRAME_HEIGHT))
    
    for frame in full_clip_frames:
        out.write(frame)
    out.release()
    
    # 5. Save the metadata
    save_metadata(event_data)
    print(f"[{datetime.now()}] Successfully saved clip: {filepath}")

def start_recording_session(
    pre_event_buffer: List[np.ndarray],
    video_capture: cv2.VideoCapture,
    event_data: Dict[str, Any]
):
    """
    Starts a new thread to handle the recording and saving process.
    """
    recording_thread = threading.Thread(
        target=_save_clip_thread,
        args=(pre_event_buffer, video_capture, event_data)
    )
    recording_thread.start()