import cv2
import os

from src import config
from src.video_buffer import VideoBuffer
from src.event_detector import simulate_event
from src.recorder import start_recording_session

def main():
    """
    Main function to run the event-based video recording system.
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(config.OUTPUT_DIR):
        os.makedirs(config.OUTPUT_DIR)

    # Initialize video capture [cite: 25]
    cap = cv2.VideoCapture(config.VIDEO_SOURCE)
    if not cap.isOpened():
        print("Error: Could not open video source.")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.FRAME_HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, config.FPS)

    # Initialize components
    buffer = VideoBuffer(buffer_size=config.BUFFER_SIZE)
    is_recording = False
    
    print("System running. Press 'e' to trigger a recording event. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Finished reading video stream or error occurred.")
            break

        # Continuously add frames to the buffer
        buffer.add_frame(frame)

        # Display the live feed
        cv2.imshow("Live Feed | Press 'e' to trigger event, 'q' to quit", frame)

        key = cv2.waitKey(1) & 0xFF

        # User interaction to simulate an event
        if key == ord('e'):
            event_data = simulate_event()
            print(f"Event triggered: {event_data}")
            
            # Get the buffer at the moment of the event
            pre_event_frames = buffer.get_buffer()
            
            # Start the recording process in a separate thread
            start_recording_session(pre_event_frames, cap, event_data)

        # Quit the application
        elif key == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()
    print("System shut down.")

if __name__ == "__main__":
    main()