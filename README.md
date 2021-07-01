# Netway-Webapp

Ce projet a pour but le déploiement d'une application de management d'infrastructure pour le compte de l'entreprise NetWay

Celle-ci englobe une architecture client-serveur échangeant par le biais d'une API.

Côté client nous retrouvons une application GUI sous TKinter offrant à l'utilisateur différente fonctionnalité en fonction de ses rôles :
- Gestion des utilisateurs (créations - modification - suppression - consultations)
- Scan de port
- Bruteforce
- Activation de script sur des machines distantes (Créations et rotations de log d'un serveur FTP)

Côté serveur, cela est geré par le framework Flask et SQLite pour les requêtes de base de données.



Pour utiliser notre application, c'est très simple : 

>Posséder Python 3.7 

`git clone https://github.com/Estebangbr/Netway-Webapp.git`

Ensuite vous devez exécuter le fichier _main.py_

`python3 main.py`

Vous voilà désormais prêts à vous connecter à la plateforme. Enjoy !