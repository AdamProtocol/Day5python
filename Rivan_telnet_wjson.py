#config using json file

import json
import telnetlib

with open('Rivan_devices.json') as f:
    buksan_file = json.load(f)


#print(buksan_file['Student_11'])
#print(buksan_file['Student_11']['switch_ip_vlan1'])

#if hirap pa sila intindihin ung concept make few more exercises

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
    read_output = tn.read_all().decode('ascii')
    print(read_output)

def initconfigdev(hostname,passw):
        command = [
            b'enable \n',
            b'configure terminal \n',
            b'Hostname ' +hostname.encode('utf-8')+passw.encode('utf-8')+b'\n',
            b'enable secret '+passw.encode('utf-8') + b'\n',
            b'service password-encryption \n',
            b'no logging console \n',
            b'no ip domain-lookup \n',
            b'line console 0  \n',
            b'password ' +passw.encode('utf-8') +b'\n',
            b'login \n',
            b'exec-timeout 0 0 \n',
            b'line vty 0 14 \n',
            b'password ' + passw.encode('utf-8') + b'\n',
            b'login \n'
            b'exec-timeout 0 0 \n'
        ]

        for i in command:
            tn.write(i)

        print('Initialized')

def pick_stud(num):
    stud = buksan_file[f'Student_{num}']
    return stud


def config_vlans(stud):
    mask = '255.255.255.0'
    command = [
        'enable',
        'configure terminal',
        'interface vlan 1',
        'no shutdown',
        f'ip address {stud["switch_ip_vlan1"]} {mask}',
        'description mgmtvlan',
        'interface vlan 1',
        'no shutdown',
        f'ip address {stud["switch_ip_vlan10"]} {mask}',
        'description wirelessvlan',
        'interface vlan 1',
        'no shutdown',
        f'ip address {stud["switch_ip_vlan100"]} {mask}',
        'description voicevlan'

    ]

    for i in command:
        #concept: you can put words infront and at the back
        i = i[:0] + "b'" + i[0:] +r"\n'"
        tn.write(i)


#executing the app
host = pick_stud('11')
#10.11.1.4
tn = telnetlib.Telnet(host["switch_ip_vlan1"])
login()
initconfigdev('myname_switch', 'cisco')
config_vlans(pick_stud(11))
end_sess()
get_output()


