import serial
import sys


def run(direction, amount):
    ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)
    print(ser.name)

    if direction == "l":
        ser.write(bytes("servo1 {}".format(amount*-1), encoding='UTF-8'))

    elif direction == "r":
        ser.write(bytes("servo1 {}".format(amount), encoding='UTF-8'))

    elif direction == "u":
        ser.write(bytes("servo2 {}".format(amount), encoding='UTF-8'))

    elif direction == "d":
        ser.write(bytes("servo2 {}".format(amount*-1), encoding='UTF-8'))

    ser.close()


if __name__ == "__main__":
    direction = sys.argv[1]
    amount = sys.argv[2]
    run(direction, amount)
