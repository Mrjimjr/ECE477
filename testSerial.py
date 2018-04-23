import serial
import time
import os
import re
from multiprocessing import Process

port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=3.0)

# LED Signal
# M ## GGG RRR BBB x
# 0 2  5   9   13  17
def LED():
	while True:
		for x in xrange(0,50):
			string = "S {:02d} 255 000 000 x".format(x)
			# print "writing " + string
			port.write(string)
			time.sleep(0.01)
		for x in xrange(0,50):
			string = "S {:02d} 000 000 255 x".format(x)
			# print "writing " + string
			port.write(string)
			time.sleep(0.01)
		for x in xrange(0,50):
			string = "S {:02d} 000 255 000 x".format(x)
			# print "writing " + string
			port.write(string)
			time.sleep(0.01)

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