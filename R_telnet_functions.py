import telnetlib
import time

host = '10.11.1.4'

#ask students to automaticaly shutdown a port

tn = telnetlib.Telnet(host)
tn.write(b'pass \n')
tn.write(b'enable \n')


tn.write(b'config t \n')
#let students finish the code
tn.write(b'interface fa0/5 \n')
tn.write(b'shutdown \n')
tn.write(b'end \n')
tn.write(b'exit \n')


#intro to function

#functions in python is like summing up all the code in one block

def login():
	tn.write(b'pass \n')
	tn.write(b'enable \n')

def interface_shut(port_num):
	tn.write(b'config t \n')
	tn.write(b'interface '+port_num.encode('ascii')+b'\n')
	tn.write(b'shutdown \n')

def end_sess():
	tn.write(b'end \n')
	tn.write(b'exit \n')

def get_output():
	tn.close()
	read_output = tn.read_all.decode('ascii')
	print(read_output)

login()
interface_shut('fa0/5')
end_sess()
get_output()

print('End Automation')