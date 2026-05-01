import socket





class DebugGameServer:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("0.0.0.0", 6767))
        self.server.listen()


        self.conn, self.addr = self.server.accept()
           

    
    def runDebugServer(self):
        while True:

            
          
            data = self.server.recv(1024).decode()
            if not data:
                break

            


        self.conn.shutdown(socket.SHUT_RDWR)
        self.conn.close()
       







def main():
    debug_server = DebugGameServer()

    try:
        debug_server.runDebugServer()
    except KeyboardInterrupt:
        print("Ctrl+C")



