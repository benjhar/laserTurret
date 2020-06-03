import json
import serial

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)
print(ser.name)

with open('movement.json') as f:
    movement = json.load(f)
    direction = movement["direction"]
    amount = movement["amount"]
    # print(movement)

if direction == "l":
    ser.write(b"servo1, ", amount)
    amount = 0

if direction == "r":
    ser.write(b"servo1, ", amount)
    amount = 0

if direction == "u":
    ser.write(b"servo2, ", amount)
    amount = 0

if direction == "d":
    ser.write(b"servo2, ", amount)
    amount = 0

ser.close()
