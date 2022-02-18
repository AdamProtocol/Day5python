#using telnet

import telnetlib
import time

#show how telnet work manualy

host = '10.1.1.4'

tn = telnetlib.Telnet(host)

tn.write(b'pass \n')
tn.write(b'enable \n')
tn.write(b'config t \n')
tn.write(b'hostname telnetpythonSwitch-11 \n')
tn.write(b'end \n')
tn.write(b'exit \n')

read_output = tn.read_all().decode('ascii')
print(read_output)

