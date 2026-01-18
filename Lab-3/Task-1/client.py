import socket

port = 6060
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)
buffer = 16
format = "utf-8"
disconnected_msg = "END"
server_socket_addr = (host_ip, port)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client.connect(server_socket_addr)

def message_to_send(message):
    message = message.encode(format)
    message_length = len(message)
    message_length = str(message_length).encode(format)
    message_length += b" "*(buffer-len(message_length))
    
    client.send(message_length)
    client.send(message)
    
    print(client.recv(2048).decode(format))
    
message_to_send(f"IP address of the client is {host_ip} and the device name is {hostname}")
message_to_send(disconnected_msg)