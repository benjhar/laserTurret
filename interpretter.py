import serial
import sys
import time


def run(direction, amount):
    ser = serial.Serial()
    ser.port = "/dev/ttyUSB0"
    ser.baudrate = 115200
    ser.timeout = 1
    ser.setDTR(False)
    # ser.setRTS(False)
    ser.open()
    time.sleep(2)
    # print(ser.name)

    if direction == "l":
        ser.write(bytes("servo1", encoding='UTF-8'))
        ser.write(bytes(f"{amount*-1}", encoding='UTF-8'))

        print(f"servo1 {amount*-1}")
        # ser.close()

    elif direction == "r":
        ser.write(bytes("servo1", encoding='UTF-8'))
        ser.write(bytes(f"{amount}", encoding='UTF-8'))

        print(f"servo1 {amount}")
        # ser.close()

    elif direction == "u":
        ser.write(bytes("servo2", encoding='UTF-8'))
        ser.write(bytes(f"{amount}", encoding='UTF-8'))

        print(f"servo2 {amount}")
        # ser.close()

    elif direction == "d":
        ser.write(bytes("servo2", encoding='UTF-8'))
        ser.write(bytes(f"{amount*-1}", encoding='UTF-8'))

        print(f"servo2 {amount*-1}")
        # ser.close()


if __name__ == "__main__":
    direction = sys.argv[1]
    amount = float(sys.argv[2])
    run(direction, amount)
