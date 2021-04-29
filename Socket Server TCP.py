import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 3000

server.bind((host, port))

server.listen(3)

clientserver, address = server.accept()
print("Connection Received from " % str(address))

message("SERVER CONNECTION ESTABLISHED! - Server")
clientserver.send(message)

clientserver.close()