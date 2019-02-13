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
    data = conn1.recv(BUFFER_SIZE)
    if not data: break
    print("received data:", data)
    conn2.send(data)  # echo
conn1.close()
conn2.close()