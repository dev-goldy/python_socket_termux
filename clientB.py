import socket

c = socket.socket()
ip = input("Enter the IP address of the server: ")
port = int(input("Enter the port number: "))
c.connect((ip, port))

while True:
    message = input("Send a message: ")
    c.send(bytes(message, "utf-8"))
    print("Message sent.")
    response = c.recv(1024).decode()
    print("Received message: ", response)

    if message.lower() == "quit":
        break

c.close()
