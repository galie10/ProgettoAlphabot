import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
                                                     #TCP

def main():
    s.connect(("192.168.0.133", 7000)) #connetto server e client

    while True:
        msg = input("Inserisci comando: ") #chiede in input un messaggio all'utente
        s.sendall(msg.encode()) #manda il messaggio al server
            
if __name__ == "__main__":
    main()