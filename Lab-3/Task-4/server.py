import socket

port = 7070
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
        print("Length od the message: ", message_length)
        
        if message_length:
            message_length = int(message_length)
            message = conn.recv(message_length).decode(format)
            if message == disconnected_msg:
                conn.send("Goodbye !".encode(format))
                print("I am terminating the cinnection with ", addr)
                connected = False
            else:
                hour = int(message)
                salary = 0
                if hour <= 40:
                    salary += hour*200
                else:
                    salary += 8000+(300*(hour-40))
                conn.send(f"Salary: {salary}".encode(format))     
    
    conn.close()     