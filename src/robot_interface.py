import socket
import json



class robotInterface:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket.connect(('127.0.0.1', 30000))
        print('Connection done')

    def sendCommand(self, x, y):
        data = {"command":"movel", 
                "target": [float(x),float(y),0,0,0,0]}
        j_data = json.dumps(data) + "\n"
        self.socket.sendall(j_data.encode('utf-8'))

    
        