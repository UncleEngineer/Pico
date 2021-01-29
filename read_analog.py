# by uncle paul
# https://youtu.be/PYOaO1yW0rY

import machine
import utime

pot = machine.ADC(26)
convert = 3.3/65535
while True:
	volt = pot.read_16()*convert
	print(volt)
	utime.sleep(2)