import socket



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostbyname('113.203.21.227'), int(input("enter port :"))))

full_msg = ''
while True:
    msg = s.recv(8).decode("utf-8")
    if len(msg) > 0:
        print(msg)

