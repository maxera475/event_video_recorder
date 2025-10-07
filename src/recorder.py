# src/recorder.py

import cv2
import json
import os
import threading
from datetime import datetime
from typing import List, Dict, Any
import numpy as np

from src import config

def save_metadata(event_data: Dict[str, Any]):
    # This function remains the same
    if not os.path.exists(config.METADATA_FILE):
        with open(config.METADATA_FILE, 'w') as f:
            json.dump([], f)

    with open(config.METADATA_FILE, 'r+') as f:
        metadata_list = json.load(f)
        metadata_list.append(event_data)
        f.seek(0)
        json.dump(metadata_list, f, indent=4)

def _save_clip_thread(
    full_clip_frames: List[np.ndarray], # <--- Receives all frames
    event_data: Dict[str, Any]
):
    print(f"[{datetime.now()}] Saving clip for event...")

    timestamp_str = datetime.fromisoformat(event_data["timestamp"]).strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp_str}_{event_data['event_type']}.mp4"
    filepath = os.path.join(config.OUTPUT_DIR, filename)
    event_data["filename"] = filename

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(filepath, fourcc, config.FPS, (config.FRAME_WIDTH, config.FRAME_HEIGHT))
    
    for frame in full_clip_frames:
        out.write(frame)
    out.release()
    
    save_metadata(event_data)
    print(f"[{datetime.now()}] Successfully saved clip: {filepath}")

def start_recording_session(
    full_clip_frames: List[np.ndarray], # <--- Pass the full clip
    event_data: Dict[str, Any]
):
    recording_thread = threading.Thread(
        target=_save_clip_thread,
        args=(full_clip_frames, event_data) # <--- Update args
    )
    recording_thread.start()