
#variables globales
URL = "https://api.openweathermap.org/data/2.5/weather"

LENGTH = 120 #taille de l'écran fictif de l'interface utilisateur
alignLeft = "left" #Aligner un texte à gauche sur l'interface en console
WELCOME = "|  Weather For All est une application qui vous permet de consulter la météo," + (" " * 15) + "|\n\t|\tdepuis chez vous.Vous pourrez y consulter des données météorologiques(température,  " + "|\n\t|\tvent,humidité...) et ce,très facilement" + (" " * 45) +  "|\n\t|\t\tAlors,allons-y !" + (" " * 60) + '|'
HELP = "|" + "Nous vous souhaitons encore la bienvenue encore sur notre application météo !".center(91) + "|\n\t|" + "Comment l'utiliser ? ".center(91) + "|\n\t|   Choisissez une section parmi les sections présentes à l'écran et réalisez les actions   |\n\t|\tdemandées pour obtenir vos résultats.".center(120) + "C'est parti !" + (" " * 34) + '|'

DATAS_FOLDER_NAME = "datas" #dossier de stockage des données de l'application notamment les historiques de recherche de l'utilisateur dans le fichier JSON <HISTORIC_FILE>
HISTORIC_FILE_NAME = "historic.json" #fichier de stockage de l'historique des recherches de l'utilisateur