import cv2
import socket
import video_frame_pb2
import threading

class VideoStream:
    def __init__(self, ip, port):
        self.UDP_IP = ip
        self.UDP_PORT = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.cap = cv2.VideoCapture(0)
        self.stop_event = threading.Event()

    def send_frame(self):
        frame_number = 0
        while not self.stop_event.is_set():
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to grab frame")
                continue

            _, buffer = cv2.imencode('.jpg', frame)
            video_frame = video_frame_pb2.VideoFrame()
            video_frame.frame_number = frame_number
            video_frame.data = buffer.tobytes()

            self.sock.sendto(video_frame.SerializeToString(), (self.UDP_IP, self.UDP_PORT))
            frame_number += 1

    def start(self):
        self.thread = threading.Thread(target=self.send_frame)
        self.thread.start()

    def stop(self):
        self.stop_event.set()
        self.thread.join()
        self.cap.release()


import time

if __name__ == "__main__":
    stream = VideoStream("YOUR_SERVER_IP", 12345)
    stream.start()

    # Run the streaming in the background for 10 seconds
    time.sleep(10)

    # Stop the streaming and clean up
    stream.stop()

    # Now you can run other tasks in parallel or even introduce more concurrency