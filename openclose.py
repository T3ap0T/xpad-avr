#! /usr/bin/python
import sys
import serial

ser = serial.Serial(sys.argv[1], 1200)
ser.close()
