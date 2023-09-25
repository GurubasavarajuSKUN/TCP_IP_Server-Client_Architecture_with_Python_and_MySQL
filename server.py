from XML import XML
import logging
import mysql.connector
import socket
from datetime import datetime


obj = XML()
dt = datetime.now()
log = logging.getLogger()
timestampStr = dt.strftime("%d-%b-%Y %H:%M:%S.%f")
logging.basicConfig(filename="log/serverLog.log",     #path for the log file
                    format='%(asctime)s %(message)s')
#log.setLevel(logging.DEBUG)                   




# Setting up database
mydb = mysql.connector.connect(
  host="******",               #name of the host
  user="*****",                # user
  password="******",           #password for db
  database="******"            #name of the schema
)
mycursor = mydb.cursor()




def server_program():
    print("Server is running")    
    log.info("Server is running")                                   #logging
    host = obj.getDetails('IP','SERVER.XML')
    port = int(obj.getDetails('PORT','SERVER.XML'))
    server_socket = socket.socket()
    server_socket.bind((host, port)) 
    server_socket.listen(10)
    conn, address = server_socket.accept()
    
    print(timestampStr+ ": Connection from: " + str(address))
    log.info(" : Connection from: " + str(address))
    
    while True:
        userData = conn.recv(1024).decode()
        if userData == 'ready':        
            sql = "SELECT * FROM bot_meta WHERE BOT_Length ='25'"    #change sal statement for your requirements
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            Data = ' '.join(map(str, myresult))
            conn.send(Data.encode())
            print(timestampStr+" : Data sent to " +str(address)+ ": "+Data) 
            log.info(" : Data sent to " +str(address)+ " : "+Data)
        else:
            error = "Invalid Reques from Client"
            log.error(error)
            conn.send(error.encode())
        
    conn.close()  


if __name__ == '__main__':
    server_program()