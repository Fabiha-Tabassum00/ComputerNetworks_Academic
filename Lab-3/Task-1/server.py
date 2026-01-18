import socket

port = 6060
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)
buffer = 16
format = "utf-8"
disconnected_msg = "END"
server_socket_addr = (host_ip, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(server_socket_addr)
server.listen()
print("Server is ready to listen")

while True:
    conn, addr = server.accept()
    print("Connected to", addr)
    
    connected = True
    while connected:
        message_length = conn.recv(buffer).decode(format)
        print("Length of the message: ", message_length)
        
        if message_length:
            message_length = int(message_length)
            message = conn.recv(message_length).decode(format)
            if message == disconnected_msg:
                conn.send("Goodbye !".encode(format))
                print("I am terminating the cinnection with ", addr)
                connected = False
            else:
                print(message)
                conn.send("Message has been received.".encode(format))            

    conn.close()