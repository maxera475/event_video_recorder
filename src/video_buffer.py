import collections

class VideoBuffer:
    """
    A class to maintain a fixed-size buffer of video frames using collections.deque.
    """
    def __init__(self, buffer_size: int):
        """
        Initializes the buffer.
        Args:
            buffer_size (int): The maximum number of frames to store.
        """
        self.buffer = collections.deque(maxlen=buffer_size)

    def add_frame(self, frame):
        """Adds a new frame to the buffer, automatically discarding the oldest."""
        self.buffer.append(frame)

    def get_buffer(self) -> list:
        """Returns the entire buffer as a list of frames."""
        return list(self.buffer)