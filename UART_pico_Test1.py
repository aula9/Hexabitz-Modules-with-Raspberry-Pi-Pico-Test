#AulaJazmati
#Test
#Hexabitz Modules with Raspberry Pi Pico Test
from machine import UART, Pin
import time
uart = UART(0, baudrate= 921600, tx=Pin(0), rx=Pin(1))  # init with given baudrate
uart.init(921600, bits=8, parity=None, stop=1)          # init with given parameters
print('-- UART Serial Test --')
print('>', end='')
txData = b'\r'
uart.write(txData.decode('utf-8'))
time.sleep(1)
txData = b'on 90 \r'
uart.write(txData.decode('utf-8'))
time.sleep(1)
rxData = bytes()
while uart.any() > 0:
    rxData = uart.readline()
    print(rxData)
    txData = b'color red 90 \r'
    uart.write(txData.decode('utf-8'))
    time.sleep(3)
    txData = b'color green 90 \r'
    uart.write(txData.decode('utf-8'))
    time.sleep(3)
    txData = b'color yellow 90 \r'
    uart.write(txData.decode('utf-8'))
    time.sleep(3)
