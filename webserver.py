import  sys
import socket

ENC = 'ISO-8859-1'

def main():
    port=28333
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    #1) Create Listening socket
    s = socket.socket()
    # 2) Allow quick restart without "Address already in use"
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #3) Bind to all local interfaces on chosen port
    s.bind(('', port))

    s.listen(5)
    print(f"Server listening on port {port}... (CTRL-C to stop)")
    while True:
        #Accept new connection
        client_socket, client_address = s.accept()
        print(f"New connection from {client_address}")

        try:
            request=b""
            while b"\r\n\r\n" not in request:
                chunk = client_socket.recv(4096)
                if not chunk:
                    break
                request += chunk
                print(f"received request:{request.decode(ENC)} from {client_address}")

            response="HTTP/1.1 200 OK\r\n"
            response += "Content-Type: text/plain\r\n\r\n"
            response += "Content-Length: 6\r\n"
            response += "Connection: close\r\n\r\n"
            response += "Hello!"

            client_socket.sendall(response.encode(ENC))
            print(f"sent response")


        finally:
            client_socket.close()

if __name__ == "__main__":
    main()
