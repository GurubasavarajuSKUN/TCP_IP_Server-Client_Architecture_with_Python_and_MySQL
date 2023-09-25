import logging
from XML import XML
import socket
from datetime import datetime
obj = XML()
dt = datetime.now()

logging.basicConfig(filename="log/clientLog.log",
                    format='%(asctime)s %(message)s')
log = logging.getLogger()
log.setLevel(logging.DEBUG)
timestampStr = dt.strftime("%d-%b-%Y %H:%M:%S.%f")


def client_program():
    host = obj.getDetails('IP','CLIENT.XML')      
    port = int(obj.getDetails('PORT','CLIENT.XML'))  
    client_socket = socket.socket()  
    client_socket.connect((host, port))  
    message = input(timestampStr+ ":  -> ")
#    log.info(" : Message sent to server : " +str(message))
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode()) 
        log.info(" : Message sent to server : " +str(message))
        data = client_socket.recv(1024).decode()  
        print(timestampStr+' : Received from server: ' + data)  
        log.info(" : Received from server: " +data)
        message = input(timestampStr+ ":  -> ")  
        log.info(" : Message sent to server : " +str(message))

    client_socket.close()  


if __name__ == '__main__':   
    client_program()