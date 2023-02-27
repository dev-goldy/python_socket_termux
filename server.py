import socket
import select

IP = "0.0.0.0"
PORT = int(input("Enter the port number to use: "))
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen(2)
print(f"Listening on {IP}:{PORT}")

clients = []
for i in range(2):
    conn, addr = server_socket.accept()
    clients.append(conn)
    print(f"Connected with client {i+1} >> {addr}")

print("Both clients are connected. Starting communication loop...")

while True:
    ready_socks, _, _ = select.select(clients, [], [])
    for sock in ready_socks:
        message = sock.recv(1024).decode()
        print("Received message: ", message)

        for c in clients:
            if c != sock:
                c.send(bytes(message, "utf-8"))

        if message.lower() == "quit":
            break

    if message.lower() == "quit":
        break

print("Closing connections...")
for c in clients:
    c.close()
server_socket.close()
