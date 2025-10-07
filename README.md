# **Offline Event-Based Video Recorder with Motion Detection**

## **Project Overview**

This project is an offline video analysis system that automatically detects motion events in a pre-recorded video file and saves clips of those events. It simulates the core logic of a smart security system that intelligently records only when significant activity occurs. The objective is to demonstrate skills in computer vision, real-time video processing, and event-driven architecture using only local libraries.

---

## **Directory Structure**

The project repository is organized as follows:

Of course. Here is the updated README.md file that reflects the new project features, such as using a video file for input and performing automatic motion detection.

Markdown

# **Offline Event-Based Video Recorder with Motion Detection**

## **Project Overview**

This project is an offline video analysis system that automatically detects motion events in a pre-recorded video file and saves clips of those events. It simulates the core logic of a smart security system that intelligently records only when significant activity occurs. The objective is to demonstrate skills in computer vision, real-time video processing, and event-driven architecture using only local libraries.

---

## **Directory Structure**

The project repository is organized as follows:

event_video_recorder/
│
├── src/
│   ├── init.py         # Makes 'src' a Python package
│   ├── config.py           # Central configuration for all parameters
│   ├── event_detector.py   # Motion detection logic
│   ├── recorder.py         # Handles the video and metadata saving process
│   └── video_buffer.py     # Manages the in-memory frame buffer
│
├── output/
│   ├── <timestamp>_motion_detected.mp4 # Example of a saved video clip
│   └── metadata.json                   # Log file for all recorded event metadata
│
├── main.py                 # Main application to run the video analysis
├── cli.py                  # Command-line tool to view recorded events
├── requirements.txt        # Project dependencies
├── sample_video.mp4        # Your input video file goes here
└── README.md               # This file.

---

## **How to Run the Project**

To run the analysis, follow these steps:

1.  **Prerequisites:** Ensure you have Python installed with the following libraries:
    * `opencv-python`
    * `numpy`

    You can install them using pip and the provided `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Setup:**
    * Clone this repository to your local machine.
    * Place your input video file (e.g., `sample_video.mp4`) in the project's root directory.
    * Open `src/config.py` and update the `VIDEO_SOURCE` variable to match your video's filename. You may also want to adjust `FPS`, `FRAME_WIDTH`, and `FRAME_HEIGHT` to match your video's properties.

3.  **Execution:**
    * Open your terminal, navigate to the project's root directory, and run the main script:
        ```bash
        python main.py
        ```
    * The script will begin processing the video file. A window will appear showing the video as it's being analyzed.
    * When motion is detected, a message will appear in the console, and a clip will be saved to the `output/` folder.
    * Press the **`q`** key at any time to stop the process.

---

## **Summary of Key Features**

1.  **Automatic Motion Detection:**
    * The system uses computer vision to automatically detect significant motion. It compares consecutive frames to identify changes, effectively finding events like a person walking or a hand waving without manual input.

2.  **Pre- and Post-Event Footage Capture:**
    * A continuous buffer is maintained to ensure that when motion is detected, the saved clip includes footage from several seconds *before* the event, providing crucial context. It also captures footage from *after* the event to show its conclusion.

3.  **Offline and Asynchronous Processing:**
    * The entire analysis runs offline with no internet connection required. Video saving is handled in a separate thread, ensuring the analysis process remains smooth and efficient, even on longer video files.

## **How It Works**

The motion detection logic is based on frame differencing:

1.  **Grayscale & Blur:** Each video frame is converted to grayscale and blurred slightly to reduce noise and improve detection accuracy.
2.  **Frame Differencing:** The system calculates the absolute difference between the current frame and the previous one. The result is an image that is black where there was no change and white or gray where pixels have changed.
3.  **Thresholding:** This difference image is converted into a pure black-and-white mask, making it easy to identify the location and shape of the motion.
4.  **Contour Detection:** The algorithm finds the outlines (contours) of all the white areas. If any contour is larger than a predefined minimum area, it is flagged as a significant motion event, and a recording is triggered.