def handle_client_connection(client_socket):
    """
    Handles the client connection by receiving a command,
    executing it, and sending back the output.
    """
    try:
        
        command = client_socket.recv(1024).decode('utf-8').strip()
        
        if command:
            
            pid = os.fork()
            
            if pid == 0:  
                
                os.dup2(client_socket.fileno(), 1)  
                os.dup2(client_socket.fileno(), 2) 
                
                
                os.execvp(command.split()[0], command.split())
            else:  
                
                client_socket.close()
    except Exception as e:
        print(f"Error handling client connection: {e}")
    finally:
        
        client_socket.close()