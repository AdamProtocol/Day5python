#main execute, config 3 devices using serial

#load day1 config

#how to do it, 
'''
-control + C to the machine then issue comand then exit the process then tell user to switch the serial cable
'''

import serial
import time

print('Welcome to Rivan CCNA Automation')
time.sleep(2)
state = input('Would you like to start the program?(y/n): ')

print('Starting configuration...')

def loadDay1(session):
	command = [
		b'enable \n',
		b'copy flash:Day1.text run \n'	
	]

	for i in command:
		session.write(i)
	time.sleep(3)

	print('Device is configured')


	#press the control + c



comlist = serial.tools.list_ports.comports()
com_num = ''
for i in comlist:
    com_num = str(i)[3:4]


def initserial(com):
    console = serial.Serial(
        port=f'COM{str(com)}',
        baudrate=9600,
        parity="N",
        stopbits=1,
        bytesize=8,
        timeout=8
    )
    return console

def pressC(session):
	cntr_c = chr(03)
	session.write(b'\n')
	session.write(cntr_c.encode('utf-8'))
	time.sleep(2)


main_session = initserial(com_num)

pressC()

main_session.write(b'\n')

switch = loadDay1(main_session)
input('Please remount console to next device\nPress Enter after remounting')

pressC()

cucm = loadDay1(main_session)
input('Please remount console to next device\nPress Enter after remounting')

pressC()

router = loadDay1(main_session)
input('Please remount console to next device\nPress Enter after remounting')



print('Device is configured')




