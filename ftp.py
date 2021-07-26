from ftplib import FTP
ftp = FTP('ftp.monsite.com', 'user', 'password')  


print(ftp.dir()) #Afficher le contenu du dossier 

ftp.mkd("test")