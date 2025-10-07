import cv2
import os
import time

from src import config
from src.video_buffer import VideoBuffer
from src.event_detector import MotionDetector 
from src.recorder import start_recording_session

def main():
    if not os.path.exists(config.OUTPUT_DIR):
        os.makedirs(config.OUTPUT_DIR)

    cap = cv2.VideoCapture(config.VIDEO_SOURCE)
    if not cap.isOpened():
        print(f"Error: Could not open video file: {config.VIDEO_SOURCE}")
        return

    buffer = VideoBuffer(buffer_size=config.BUFFER_SIZE)
    detector = MotionDetector() 

    print("Processing video file. Looking for motion events...")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Finished processing video file.")
            break

        # Continuously add frames to the buffer
        buffer.add_frame(frame)

        # Use the motion detector on every frame
        event_data = detector.detect(frame)

        if event_data:
            # Motion was detected!
            pre_event_frames = buffer.get_buffer()
            
            # Now, gather the post-event frames directly from the video file
            post_event_frames = []
            for _ in range(config.POST_EVENT_FRAMES):
                ret, post_frame = cap.read()
                if not ret:
                    break
                post_event_frames.append(post_frame)
            
            # Combine them into a single clip
            full_clip_frames = pre_event_frames + post_event_frames
            
            # Start a thread to save the clip without blocking
            start_recording_session(full_clip_frames, event_data)
        
        # Optional: Display the video feed while processing
        cv2.imshow("Processing Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
             break

    cap.release()
    cv2.destroyAllWindows()
    print("System shut down.")

if __name__ == "__main__":
    main()