def tri_selection(tab):
   for i in range(len(tab)):
      # Trouver le min
       min = i
       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j
                
       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp
   return tab
# Programme principale pour tester le code ci-dessus
tab = [98, 45, 178, 32, 45, 79, 65,654]
 
tri_selection(tab)
 
print ("Le tableau trié est:")
for i in range(len(tab)):
    print ("%d" %tab[i])

    #Fin du script du tableau