liste = ['a','b','c','d','e','f','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #Definission de la liste - on peut ajouter les caractères spéciaux etc...



def bruteforce(word, length): #fonction bruteforce
    if length <= 7: #Si taille du mot de passe inférieur ou egal a 7 on peut commencer le bruteforce
        for letter in liste:
            if mdp == word + letter: 
                print("Vous avez trouvé le mdp est " + word + letter) # Si le mdp = bruteforce on s'arrête
            else:
                #print(word + letter) #Afficher chaque test
                bruteforce(word + letter, length + 1) #Sinon on test la combinaison suivante


mdp = input("Entrez votre mot de passe : ")
bruteforce('', 1)


