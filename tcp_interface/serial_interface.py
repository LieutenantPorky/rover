import serial
import io

ser = serial.Serial('/dev/ttyACM0', timeout = 1)
ser.baudrate = 9600

while True:
    ser.write(b'a')
    print(ser.read(size = 4))
