import uuid
import socket
import getpass

def sync():
    devicename = socket.gethostname()
    loc_ip = socket.gethostbyname(devicename)
    macaddr = hex(uuid.getnode())
    user = getpass.getuser()
    print("-" * 40)
    print("Debug test version")
    print("-" * 40)

    print("Host name:", devicename)
    print("IP is:", loc_ip)
    print("MacAddress is:", macaddr)
    print("Username is:", user)

sync()