import socket

buffer = 100

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# server_addr = ("localhost", 4000)
server_addr = ("192.168.1.35", 4000)
print(f"server started on {server_addr[0]} on port {server_addr[1]}")
server_socket.bind(server_addr)

while True:
    print("listening...")
    
    message, client_addr = server_socket.recvfrom(buffer)
    message = message.decode("utf-8")
    print(f"message from {client_addr}:\n{message}")

    if message:
        message_answer = f"echo! {message}"
        message_sent = server_socket.sendto(message_answer.encode("utf-8"), client_addr)
        print(f"echoed to {client_addr}:\nbytes = {message_sent}")