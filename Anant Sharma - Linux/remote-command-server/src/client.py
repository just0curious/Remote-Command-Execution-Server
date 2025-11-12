import socket

def main():
    
    server_address = ('localhost', 5000)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect(server_address)
        print("Connected to the server. You can send commands.")
        
        while True:
            
            command = input("Enter command: ")
            if command.lower() in ['exit', 'quit']:
                print("Exiting client.")
                break
            
            
            client_socket.sendall(command.encode())
            
            
            response = b""
            while True:
                part = client_socket.recv(4096)
                response += part
                if len(part) < 4096:
                    break
            
            
            print("Output from server:\n", response.decode())
    
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()