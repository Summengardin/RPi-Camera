from setuptools import setup, find_packages

setup(
    name="RPi-Camera",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'picamera',
        'protobuf'
    ],
    entry_points={
        'console_scripts': [
            'send_camerastream=RPi_Camera.UDP_stream:main'
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="Send Raspberry Pi camera stream over UDP using protobuf.",
    license="MIT",  # Or any other license you want to use
    keywords="raspberry pi camera udp protobuf",
    url="http://github.com/yourusername/raspberrypi_udp_camerastream",  # Project URL if available
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Video",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
