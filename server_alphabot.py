import classe_alphabot as alfa
import socket, sqlite3
import time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
bot = alfa.AlphaBot() #la variabile bot crea l'oggetto riferimento alla classe dell'Alphabot
                                                     #TCP
s.bind(("0.0.0.0",7000)) 
s.listen()
connection, address = s.accept()
print("Connessione stabilita.")

con = sqlite3.connect("Movimenti.db") #connessione del database con il modulo sqlite3
cur = con.cursor() #cur fornisce una vista consistente dei dati della tabella

while(True):
    msg = connection.recv(4096)#4096 la dimensioni in byte del buffer di ricezione
    msg = msg.decode() #decodifico il messaggio ricevuto dal client
    print(msg)
    #in base al comando inviato esegue diversi movimenti
    if int(msg) == 1:
        res = cur.execute(f"SELECT MOVIMENTO FROM MOVIMENTI WHERE ID={msg}") #seleziono i dati interessati con una query in base all'id del dato(messaggio in input)
        lista = res.fetchone() #prendo solo i valori relativi al msg
        print(lista)

        movs = lista[0].split(";") #splitto la tupla con il punto e virgola e li assegno ad una lista
        print(movs)
            
        for movimento in movs: #per ogni movimento nella lista dei movimenti
            movimenti = []
            movimenti = movimento.split(" ") #splitto movimento e tempo del movimento
            tempo = float(movimenti[1])
            if (movimenti[0] == "forward" or movimenti[0]== "avanti" or movimenti[0] == "w"):
                bot.forward()
                time.sleep(tempo) #tempo di esecuzione del movimento
                bot.stop()
            elif (movimenti[0] == "backward" or movimenti[0] == "indietro" or movimenti[0] == "s"):
                bot.backward()
                time.sleep(tempo)
                bot.stop()
            elif (movimenti[0] == "left" or movimenti[0] == "sinistra" or movimenti[0] == "a"):
                bot.left()
                time.sleep(tempo)
                bot.stop()
            elif (movimenti[0] == "right" or movimenti[0] == "destra" or movimenti[0] == "d"):
                bot.right()
                time.sleep(tempo)
                bot.stop()
            elif (movimenti[0] == "stop" or movimenti[0] == "fermo" or movimenti[0] == "q"):
                bot.stop()
    elif int(msg) == 2:
        res = cur.execute(f"SELECT MOVIMENTO FROM MOVIMENTI WHERE ID={msg}")
        lista = res.fetchone()
        print(lista)

        movs = lista[0].split(";")
        print(movs)
            
        for movimento in movs:
            movimenti = []
            movimenti = movimento.split(" ")
            tempo = float(movimenti[1])
            if (movimenti[0] == "forward" or movimenti[0]== "avanti" or movimenti[0] == "w"):
                bot.forward()
                time.sleep(tempo) 
                bot.stop()
            elif (movimenti[0] == "backward" or movimenti[0] == "indietro" or movimenti[0] == "s"):
                bot.backward()
                time.sleep(tempo)
                bot.stop()
            elif (movimenti[0] == "left" or movimenti[0] == "sinistra" or movimenti[0] == "a"):
                bot.left()
                time.sleep(tempo)
                bot.stop()
            elif (movimenti[0] == "right" or movimenti[0] == "destra" or movimenti[0] == "d"):
                bot.right()
                time.sleep(tempo)
                bot.stop()
            elif (movimenti[0] == "stop" or movimenti[0] == "fermo" or movimenti[0] == "q"):
                bot.stop()
    elif int(msg) == 3:
        #i dati inserendo il 3 vengono inseriti manualmente uno alla volta
        while(True):
            msg1 = connection.recv(4096)#4096 la dimensioni in byte del buffer di ricezione
            msg1 = msg1.decode() 
            ls = msg1.split(" ")
            tempo = float(ls[1])

            if (ls[0] == "forward" or ls[0] == "avanti" or ls[0] == "w"):
                bot.forward()
                time.sleep(tempo) #tempo di esecuzione del movimento
                bot.stop()
            elif (ls[0] == "backward" or ls[0] == "indietro" or ls[0] == "s"):
                bot.backward()
                time.sleep(tempo)
                bot.stop()
            elif (ls[0] == "left" or ls[0] == "sinistra" or ls[0] == "a"):
                bot.left()
                time.sleep(tempo)
                bot.stop()
            elif (ls[0] == "right" or ls[0] == "destra" or ls[0] == "d"):
                bot.right()
                time.sleep(tempo)
                bot.stop()
            elif (ls[0] == "x" or ls[0] == "fermo" or ls[0] == "q"):
                bot.stop()
            else: pass

    s.close() #chiudo la comunicazione del socket