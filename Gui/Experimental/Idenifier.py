import uuid
import socket
import getpass

import re

def sync():
    device_name = socket.gethostname()
    loc_ip = socket.gethostbyname(device_name)
    mac_addr = hex(uuid.getnode())
    user = getpass.getuser()
    print("-" * 40)
    print("Debug test version")
    print("-" * 40)

    print("Host name:", device_name)
    print("IP is:", loc_ip)
    print("MacAddress is:", mac_addr)
    print("Username is:", user)


sync()