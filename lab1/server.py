import socket

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('localhost', 65432))  
        server_socket.listen()
        print("服务器启动，等待连接...")
        
        conn, addr = server_socket.accept()  
        with conn:
            print(f"连接来自 {addr}")
            with open('received_mock_keylogger_data.txt', 'wb') as f:
                while True:
                    data = conn.recv(1024)  
                    if not data:
                        break  
                    f.write(data)  

if __name__ == "__main__":
    main()
