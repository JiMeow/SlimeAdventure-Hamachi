import socket


HOST = '0.tcp.ap.ngrok.io'
PORT = 13561

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    data = s.recv(1024)
    reply = data.decode("utf-8")
    print("server:", reply)
    inp = input()
    s.send(str.encode(inp))
