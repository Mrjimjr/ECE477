import serial
import time

port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=3.0)

# LED Signal
# M ## GGG RRR BBB x
# 0 2  5   9   13  17

while True:
	for x in xrange(0,49):
		string = "S {:02d} 255 000 000 x".format(x)
		# print "writing " + string
		port.write(string)
		time.sleep(0.01)
	for x in xrange(0,49):
		string = "S {:02d} 000 000 255 x".format(x)
		# print "writing " + string
		port.write(string)
		time.sleep(0.01)
	for x in xrange(0,49):
		string = "S {:02d} 000 255 000 x".format(x)
		# print "writing " + string
		port.write(string)
		time.sleep(0.01)

	time.sleep(1)
	rcv = port.read(12)
	print rcv
	# port.write("\r\nYou sent:" + repr(rcv))
