import socket
import threading

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

def client_handle(conn, addr):
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
                vowels = "aeiouAEIOU"
                counter = 0
                for i in message:
                    if i in vowels:
                       counter+=1
                if counter==0:
                     conn.send("Not enough vowels".encode(format))
                elif counter <= 2:
                     conn.send("Enough vowels I guess".encode(format))
                else:
                     conn.send("Too many vowels".encode(format))     
                     
    conn.close()
    
while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=client_handle,args=(conn,addr))
    thread.start()
