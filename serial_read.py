import serial

def read_until(until):
	out=""
	while True:
		data = ser.read(1) #read one byte from the serial input
		if len(data)>0:
			out += data
		if until in out:
			break
		if data == '':
			break
	return out

def read_empty():
	out = ""
	while True:
		data = ser.read(1)
		if len(data) > 0:
			out += data
		else:
			break
	return out
