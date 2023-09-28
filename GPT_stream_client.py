# pi_camera_stream_client.py

import socket
import cv2
import numpy as np
import picamera
import picamera.array
import time
import argparse

parser = argparse.ArgumentParser(description='Rapid stream client')

parser.add_argument('--host', type=str, default='localhost',
                    help='Host IP address')
parser.add_argument('--port', type=int, default=8000,
                    help='Port number')

args = parser.parse_args()


# UDP setup
UDP_IP = args.host
UDP_PORT = args.port
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Camera setup
WIDTH = 320
HEIGHT = 240

with picamera.PiCamera() as camera:
    camera.resolution = (WIDTH, HEIGHT)
    with picamera.array.PiRGBArray(camera) as stream:
        time.sleep(2)  # Warm up
        for _ in camera.capture_continuous(stream, 'bgr', use_video_port=True):
            frame = stream.array

            # Convert frame to JPEG and then to byte array
            is_success, buf = cv2.imencode(".jpg", frame)
            if is_success:
                sock.sendto(buf.tobytes(), (UDP_IP, UDP_PORT))

            # Clear stream for the next frame
            stream.truncate(0)
