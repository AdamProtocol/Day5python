#Exercise config the initial config, see handout1 
#lahat students check config ng switch by doing a show run command


import serial
import serial.tools.list_ports
import time



comlist = serial.tools.list_ports.comports()
com_num = ''
for i in comlist:
    com_num = str(i)[3:4]


console_session = serial.Serial(
        port=f'COM{str(com_num)}',
        baudrate=9600,
        parity="N",
        stopbits=1,
        bytesize=8,
        timeout=8
    )

#this will press control + c

c = chr(3)
console_session.write(b'\n')
console_session.write(c.encode('utf-8'))
console_session.write(b'\n')
time.sleep(2)

console_session.write(b'enable \n')
console_session.write(b'config t \n')
console_session.write(b'hostname LEAF-11 \n')
console_session.write(b'enable secret pass \n')
#this method is inefficient 
#use listing method
#show the general idea of listing
command = [
	b'service password-encryption \n',
	b'no logging console \n',
	b'no ip domain-lookip \n',
	b'line console 0 \n',
	b'password pass \n',
	b'login \n',
	b'exec-timeout 0 0 \n',
	b'line vty 0 14 \n',
	b'password pass \n',
	b'login \n',
	b'exec-timeout 0 0 \n',
	b'int gi0/0/0',
	b'no shutdown \n',
	b'ip add 10.11.11.4 2555.255.255.0 \n',
	b'interface vlan 1 \n',
	b'no shutdown \n',
	b'ip add 10.11.1.4 255.255.255.0 \n',
	b'description'
	b'interface vlan 10 \n',
	b'no shutdown \n',
	b'ip address 10.11.10.4 255.255.255.0 \n',
	b'description MGMTVLAN \n',
	b'interface vlan 100 \n',
	b'no shutdown \n',
	b'ip address 10.11.100.4 255.255.255.0 \n',
	b'description VOIVEVLAN \n'
]

for i in command:
	time.sleep(.2)
	console_session.write(i)

console_session.write(b'end \n')
console_session.close()

print('AUTOMATION ENDED')



