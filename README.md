# **Event-Based Video Recorder**

## **Project Overview**

This project is a prototype system that demonstrates event-based video recording, simulating features found in smart security cameras or vehicle dashcams. The objective is to showcase skills in real-time video processing, event-driven architecture, and concurrent programming. The system uses a mock AI event detector to trigger the saving of video clips that capture footage from both *before* and *after* a detected event.

---

## **Directory Structure**

The project repository is organized as follows:
event_video_recorder/
│
├── src/
│   ├── init.py         # Makes 'src' a Python package
│   ├── config.py           # Central configuration for all parameters
│   ├── event_detector.py   # Mock event detection logic
│   ├── recorder.py         # Handles the video and metadata saving process
│   └── video_buffer.py     # Manages the in-memory frame buffer
│
├── output/
│   ├── <timestamp>_manual_trigger.mp4  # Example of a saved video clip
│   └── metadata.json                   # Log file for all recorded event metadata
│
├── main.py                 # Main application to run the video capture system
├── cli.py                  # Command-line tool to view recorded events
├── requirements.txt        # Project dependencies
└── README.md               # This file.

---

## **How to Run the Project**

To run the system, follow these steps:

1.  **Prerequisites:** Ensure you have Python installed with the following libraries:
    * `opencv-python`
    * `numpy`

    You can install them using pip and the provided `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Setup:**
    * Clone this repository to your local machine.
    * The `output/` directory will be created automatically on the first run.

3.  **Execution:**
    * Open your terminal, navigate to the project's root directory, and run the main script:
        ```bash
        python main.py
        ```
    * A window will appear showing your live webcam feed.
        * Press the **`e`** key to simulate an AI event and trigger a recording.
        * Press the **`q`** key to shut down the application.
    * The script will automatically save 30-second video clips and update the `metadata.json` file in the `output/` directory.

---

## **Summary of Key Features**

1.  **Continuous Pre-Event Buffering:**
    * The system maintains a constant, rolling 15-second buffer of video in memory. This ensures that when an event is triggered, the saved clip includes the critical moments leading up to it.

2.  **Asynchronous Event-Based Recording:**
    * Upon event detection, the recording and file-saving processes are offloaded to a separate thread. This is a key design choice that prevents the live video feed from freezing or lagging, ensuring the system remains responsive.

3.  **Comprehensive Metadata Logging:**
    * Each video clip is accompanied by a structured JSON log entry in `metadata.json`. This log includes the event type, a precise timestamp, the video filename, and simulated GPS coordinates, making the data easy to parse and analyze later.

