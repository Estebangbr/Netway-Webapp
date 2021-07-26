
import socket
import threading
from queue import Queue


def scan():
    
    print_lock = threading.Lock()

    target ='localhost' # Ciblage de l'analyse des ports ouverts



    def scan_range(port): # Création de la fonction scan
    
        list = []
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Création d'un socket pour la connexion avec le serveur en local
        try:
            result = sock.connect_ex((target, port)) # Définir sur laquelle les ports vont écouter
            with print_lock:
                list.append(port) # Indication des ports qui sont ouverts
            result.close()
        except:
            pass
        
    
    
    def threader (): # Définir le threading
        while True:
            worker = q.get()
            scan_range(worker)
            q.task_done()

    q = Queue ()

    for x in range (60):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()

    for worker in range (1,101): # Effectuer une recherche des ports ouverts
        q.put(worker)

    q.join()

    
print(list)


scan()
