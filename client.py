import socket

class Message:
    def __init__(self, sender, receiver, text):
        self.sender = sender
        self.receiver = receiver
        self.text = text

    def display_message(self):
        print(f"from {self.sender} to {self.receiver}:\n{self.text}")
        

buffer = 100

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_addr = ("localhost", 4000)

message = b"hello there!"

try:
    sent = client_socket.sendto(message, server_addr)

    print("waiting for answer...")
    
    server_answer, server_addr = client_socket.recvfrom(buffer)
    server_answer = server_answer.decode("utf-8")
    print(f"message from {server_addr}:\n{server_answer}")

finally:
    print("connection closed")
    client_socket.close()