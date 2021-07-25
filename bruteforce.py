liste = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9'] #Definission de la liste - on peut ajouter les caractères spéciaux etc...

def bruteforce(word, length): #fonction bruteforce
    if length <= 6: #Si taille du mot de passe inférieur ou egal a 5 on peut commencer le bruteforce
        for letter in liste:
            if mdp == word + letter: 
                print("Vous avez trouvé le mdp est " + word + letter) # Si le mdp = bruteforce on s'arrête
            else:
                print(word + letter) #Afficher chaque test
                bruteforce(word + letter, length + 1) #Sinon on test la combinaison suivante


mdp = input("Entrez votre mdp : ") #Saisir le mot de passe à trouver
bruteforce('', 1)

