# coding:utf-8

######################################################
### Bonjour Olivier                                ###
### Mes commentaires sont précédés de trois dièses ###
######################################################

### Il faut mettre l'extension .py à ton nom de fichier :)

from eureka import articles ### Oh! Bravo!
### Je ne vous avais pas parlé de la commande import encore! :)
### Tu as lu la documentation que je vous ai donnée. Super!

article1 = [] ### À quoi sert cette variable? Ou devait-elle servir?

for article in articles:

	article = article.split(",")

	if len(article) >= 4:

		media = article[0]

		section = article[1]

		page = article[3]

		mot = article[2].split()[4]

	print(media,section,page,mot)

### Tout va assez bien jusqu'ici.
### Utiliser la méthode «.strip()» permet de se débarrasser d'espaces superflus, aussi.

### Le «print» ci-dessous n'imprime qu'une seule ligne parce qu'il se trouve à l'extérieur de la boucle «for» ci-dessus.
### Il imprime les informations relatives au dernier article traité par la boucle «for».
print("Cet article a été publié par " + media + " dans la section " + section + ". Sa longueur est de " + mot + " mots et il apparaît à la page " + page + ".")


# J'ai vraiment bloqué à la dernière consigne de l'exercice. Je crois mal maîtriser la commande .count
#Ce n'est vraiment pas facile tout ça et j'ai hâte de voir le corrigé au prochain cours!
# J'ai consulté plusieurs documents sur Internet ainsi que des vidéos YouTube, mais ceux-ci ne sont souvent pas adaptés aux listes et au journalisme.

### Pour la suite, voir le corrigé :)
### En gros, il s'agissait de créer des compteurs (un pour chaque média) et de les augmenter de un dans ta boucle for si la variable «media» correspond au nom du média que tu comptes.