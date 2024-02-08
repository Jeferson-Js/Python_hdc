import socket 

host = input('Digite : ')
ports = [21,22,25,80,443,445,3306]

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.2)
    client.connect_ex((host, port))
    if client.connect_ex((host, port)) == 0:
        print(f"Port {port} is \033[92m OPEN \033[0m")
    else: 
        print(f"Port {port} is \033[91m CLOSED \033[0m")
    client.close()