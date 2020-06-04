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
    ser.write(bf"servo1 {-amount}")

if direction == "r":
    ser.write(bf"servo1 {amount}")

if direction == "u":
    ser.write(bf"servo2 {amount}")

if direction == "d":
    ser.write(bf"servo2 {-amount}")

ser.close()
