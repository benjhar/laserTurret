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
    ser.write(bytes("servo1 {}".format(amount*-1), encoding='UTF-8'))

if direction == "r":
    ser.write(bytes("servo1 {}".format(amount), encoding='UTF-8'))

if direction == "u":
    ser.write(bytes("servo2 {}".format(amount), encoding='UTF-8'))

if direction == "d":
    ser.write(bytes("servo2 {}".format(amount*-1), encoding='UTF-8'))

ser.close()
