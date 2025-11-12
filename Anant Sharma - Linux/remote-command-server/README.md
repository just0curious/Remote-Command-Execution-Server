# Remote Command Execution Server

This project implements a simple remote command execution server in Python. The server listens for incoming TCP connections, executes commands sent by clients, and returns the output back to the clients.

## Project Structure

```
remote-command-server
├── src
│   ├── server.py       # The remote command execution server
│   ├── client.py       # The client that connects to the server
│   └── utils.py        # Utility functions for socket handling and output formatting
├── requirements.txt     # List of dependencies required for the project
├── README.md            # Documentation for the project
└── examples.txt         # Example terminal commands to demonstrate functionality
```

## Setup Instructions

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required dependencies listed in `requirements.txt` (if any).

## Usage

### Starting the Server

To start the server, open a terminal and run:

```
python3 src/server.py
```

The server will start listening for incoming connections on a specified port (default is 5000).

### Connecting as a Client

In another terminal, run the client:

```
python3 src/client.py
```

You will be prompted to enter commands. For example:

```
Enter command: ls
Enter command: pwd
Enter command: date
```

The server will execute these commands and return the output to the client.

## How It Works

1. **Socket Creation**: The server creates a TCP socket and binds it to a specified port (e.g., 5000) to listen for incoming connections.
2. **Listening for Connections**: The server enters a loop, waiting for clients to connect.
3. **Forking**: When a client connects, the server forks a child process using `os.fork()` to handle the command execution.
4. **Redirection**: In the child process, `os.dup2()` is used to redirect the standard output and standard error to the client socket.
5. **Command Execution**: The server executes the received command using `os.execvp()`, which replaces the child process with the command being executed.
6. **Communication**: The output (stdout and stderr) of the command is sent back to the client through the socket, and the connection is closed after the command execution is complete. The parent process continues to listen for new connections.

## Example Commands

To demonstrate that the project works, you can use the following commands in the terminal:

- **Terminal 1**: Start the server
  ```
  python3 src/server.py
  ```

- **Terminal 2**: Connect as client and send commands
  ```
  python3 src/client.py
  Enter command: ls
  Enter command: pwd
  Enter command: date
  ```

This will show the output of each command executed on the server, returned to the client.