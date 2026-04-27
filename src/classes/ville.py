from src.classes.Timer import time # pour sauvegarder la date

class Ville:
    def __init__(self, jsondata):
        self.country = jsondata.get("sys", {}).get("country", "Pays non reconnu")
        self.localisation = jsondata.get("name","Ville inconnue")
        self.temperature = jsondata.get("main", {}).get("temp")
        self.seaLevel = jsondata.get("main", {}).get("sea_level")
        self.humidite = jsondata.get("main", {}).get("humidity")
        self.ressenti = jsondata.get("main", {}).get("feels_like")
        self.ciel = jsondata.get("weather", [{}])[0].get("description")
        self.vent = jsondata.get("wind", {}).get("speed")
        self.nuages = jsondata.get("clouds", {}).get("all")
        self.fuseau = jsondata.get("timezone")

    def getInfos(self):
        return {
            "Localisation": self.localisation + ", " + self.country,
            "Temperature": str(round(self.temperature)) + "°C",
            "Niveau de la mer": str(self.seaLevel) + "m",
            "Humidite": str(self.humidite) + "%",
            "Ressenti": str(self.ressenti) + "°C",
            "Ciel": self.ciel,
            "Vent": str(self.vent) + "m/s",
            "Nuages": str(self.nuages) + "%",
            "Fuseau Horaire": "UTC + " + str(self.fuseau // 3600)
        }
    
    def toJSON(self):
        TIME_KEEPER = time()
        return {
            "code_pays": self.country,
            "localisation": self.localisation,
            "temperature": self.temperature,
            "seaLevel": self.seaLevel,
            "humidite": self.humidite,
            "ressenti": self.ressenti,
            "ciel": self.ciel,
            "vent": self.vent,
            "nuages": self.nuages,
            "fuseau": self.fuseau,
            "date" : TIME_KEEPER.getFormalTime()
        }