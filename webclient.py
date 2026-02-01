import sys
import socket
ENC= "ISO-8859-1"

#example on command line:
#python webclient.py example.com 8080


def main():
    if len(sys.argv) < 2:
        print("Usage: python webclient.py <host> [port]")
        return
    host = sys.argv[1]
    port=80
    #if the user gave the port herself
    if len(sys.argv) >2 :
        port = int(sys.argv[2])

    print("Connecting to host:%s on port:%d" % (host, port))

    s=socket.socket()
    try:
        s.connect((host, port))

        request=(
            f"GET / HTTP/1.1\r\n"
            f"Host: {host}\r\n"
            f"Connection: close\r\n"
            f"\r\n"

        )
        s.sendall(request.encode(ENC))
        response = b""
        while True:
            chunk = s.recv(4096)
            if not chunk:
                break
            response += chunk

        print(response.decode(ENC))
    finally:
        s.close()

if __name__ == "__main__":
    main()