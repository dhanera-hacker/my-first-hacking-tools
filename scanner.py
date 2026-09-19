import socket

target = input("Kiska IP scan karna hai? ")
print("Scanning", target)

for port in [22, 80, 443, 8080]:
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print("Port", port, "is OPEN")
    else:
        print("Port", port, "is CLOSED")
    s.close()
