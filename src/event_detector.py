import cv2
import datetime
import random

class MotionDetector:
    def __init__(self, min_area=500):
        self.previous_frame = None
        self.min_area = min_area 

    def detect(self, frame):
        # 1. Prepare the frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        # 2. If this is the first frame, initialize it
        if self.previous_frame is None:
            self.previous_frame = gray
            return None

        # 3. Compute the difference between the current and previous frame
        frame_delta = cv2.absdiff(self.previous_frame, gray)
        thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]

        # 4. Dilate the thresholded image to fill in holes
        thresh = cv2.dilate(thresh, None, iterations=2)

        # 5. Find contours (outlines of moving objects)
        contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        motion_detected = False
        for contour in contours:
            # If a contour is too small, ignore it
            if cv2.contourArea(contour) < self.min_area:
                continue
            # Otherwise, we have found significant motion
            motion_detected = True
            break # No need to check other contours

        # 6. Update the previous frame
        self.previous_frame = gray

        if motion_detected:
            print("Motion Detected!")
            # Return an event dictionary if motion is found
            return {
                "event_type": "motion_detected",
                "timestamp": datetime.datetime.now().isoformat(),
                "gps_coordinates": {
                    "latitude": round(random.uniform(28.4, 28.8), 6),
                    "longitude": round(random.uniform(77.0, 77.4), 6)
                }
            }
        
        return None # Return None if no motion is found