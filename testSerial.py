import serial
import time
import os
import re
import random
from multiprocessing import Process, Array

# port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=3.0)

# LED Signal
# M ## GGG RRR BBB x
# 0 2  5   9   13  17



def LED():
	port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=3.0)

	global RGB_MODE
	global RGB_COLOR

	while True:
		for x in xrange(0,50):
			string = "S {:02d} {} x".format(x, RGB_COLOR[x])
			# print "writing " + string
			port.write(string)
			time.sleep(0.01)
		
		# Blink LEDs
		for x in xrange(0,50):
			if RGB_MODE[x] == 2:
				string = "S {:02d} 000 000 000 x".format(x)
				# print "writing " + string
				port.write(string)
			time.sleep(0.01)
		rcv = port.readline().rstrip()
		# print rcv
		try:
			xLoc = re.search(r'X([^X]*)', rcv).group(1)
			xLocInt = round(int(xLoc)) / 2
			cmd = "xdotool mousemove {} {}".format(xLocInt, 300)
			# print cmd
			# Move mouse to x y location
			# os.system(cmd)
			# Left Click
			# os.system("xdotool click 1")
		except:
			pass
	# time.sleep(1)
	# port.write("\r\nYou sent:" + repr(rcv))

def mouse():
	time.sleep(1)
	while True:
		time.sleep(0.01)
		rcv = 0
		# rcv = port.read(32)
		rcv = port.readline().rstrip()
		# print rcv
		try:
			xLoc = re.search(r'X([^X]*)', rcv).group(1)
			xLocInt = round(int(xLoc)) / 2
			cmd = "xdotool mousemove {} {}".format(xLocInt, 300)
			# print cmd
			# Move mouse to x y location
			# os.system(cmd)
			# Left Click
			# os.system("xdotool click 1")
		except:
			pass
		

if __name__ == '__main__':
	mp = Process(target=mouse)
	Lp = Process(target=LED)

	mp.start()
	Lp.start()

	mp.join()
	Lp.join()