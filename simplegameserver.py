import socket


TCP_IP = socket.gethostname()
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn1, addr = s.accept()
conn2, addr2 = s.accept()
print('Connection address:', addr)
print('Connection2 address:', addr2)
while 1:
    game1 = conn1.recv(BUFFER_SIZE)
    game2 = conn2.recv(BUFFER_SIZE)
    if not game1 or not game2: break
    print("received data:", game1)
    print("received data:", game2)
    conn2.send(game1)
    conn1.send(game2)
conn1.close()
conn2.close()