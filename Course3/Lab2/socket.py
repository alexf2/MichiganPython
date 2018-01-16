from socket import socket, AF_INET, SOCK_STREAM

for i in [108,105,110,101]:
    print (chr(i), end='')
print(ord('G'))
exit()

sock = socket(AF_INET, SOCK_STREAM)
sock.connect( ('data.pr4e.org', 80) )

try:
    sock.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode())

    while True:
        data = sock.recv(1024)
        if (len(data) < 1):
            break
        print(data.decode(), end='')
finally:
    sock.close()
