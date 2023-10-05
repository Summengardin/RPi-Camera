#!bin/bash

sudo apt update
sudo apt install -y i2c-tools python3-smbus

echo "pip3 install sparkfun-qwiic sparkfun-pi-servo-hat"
pip3 install sparkfun-qwiic sparkfun-pi-servo-hat
