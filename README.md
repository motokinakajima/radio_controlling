# radio controller
This is a program that I used for controlling a ship.

We used a raspberry pi, arduino and a computer running a python program.
First, the python program on the computer sends data to the raspberry pi using socket through wifi.
Next, the raspberry pi sends the data to the arduino using serial communication.
Last, the arduino sends electrical commands to the motors on the ship.
