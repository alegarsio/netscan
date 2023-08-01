import ipaddress , socket  , sys , subprocess,colorama,datetime
from colorama import Fore
colorama.init(autoreset=True)
date = datetime.datetime.now()
user = socket.gethostname()
address = socket.gethostbyname(user)
print(Fore.LIGHTCYAN_EX + f"""
 _  _       _                       
| \| | ___ | |_  ___ __  __ _  _ _     https://github/alegarsio/
| .  |/ -_)|  _|(_-// _|/ _` || ' \    Address : {address}
|_|\_|\___| \__|/__/\__|\__/_||_||_|

Usage : Python3 netscan.py (network/subnet) (port)\n 
{Fore.LIGHTRED_EX}"""f"Welcome to netscan {user} {date} ")

import socket
import ipaddress
import subprocess , colorama
colorama.init(autoreset=True)
from colorama import Back
if sys.platform.startswith('win'.lower()) : print(f'{Back.LIGHTRED_EX} Feature may be not available !')
def is_port_open(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
            return True
    except (socket.timeout, ConnectionRefusedError):
        return False

def scan_network(ip_range, ports):
    active_hosts = []
    for ip in ipaddress.IPv4Network(ip_range):
        if subprocess.call(["ping", "-c", "1", str(ip)]) == 0: 
            active_hosts.append(str(ip))

    open_ports = {}
    for host in active_hosts:
        open_ports[host] = [port for port in ports if is_port_open(host, port)]

    return open_ports


network = sys.argv[1]
common_ports = [int(sys.argv[2])]

try:
    import time
    result = scan_network(network, common_ports)
    print(result)
    time.sleep(1)
except KeyboardInterrupt : pass
except IndexError : print('Invalid argument')