#Using pyserial 


import serial
import serial.tools.list_ports
import time

#get the com number and save it to com_num

comlist = serial.tools.list_ports.comports()
com_num = ''
for i in comlist:
    com_num = str(i)[3:4]

#openning a serial session
console_session = serial.Serial(
        port=f'COM{str(com_num)}',
        baudrate=9600,
        parity="N",
        stopbits=1,
        bytesize=8,
        timeout=8
    )


#sending data to it

console_session.write(b'\n')

#this will press control + c

c = chr(3)

console_session.write(c.encode('utf-8')) #self study mo to pag di mo nagets, break down the process each word

console_session.write(b'\n')
time.sleep(2)

console_session.write(b'enable \n')
console_session.write(b'config t \n')
#let the students write the code, time it for 5 mins
console_session.write(b'Hostname PythonLEAF \n')
#need to end the session so that the config will push
console_session.write(b'end \n')
console_session.close()


#(BUKAS BAGONG FILE)Then give an exercise on how to do it again but on the CUCM, note dapat tumahimik sya ng hindi mo tinatrpe






