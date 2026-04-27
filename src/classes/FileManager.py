
import json
from pathlib import Path # pour avoir le chemin des fichiers de façon fiable
from src.Globals import DATAS_FOLDER_NAME
from src.Globals import HISTORIC_FILE_NAME

    
def get_historic_file_path():

    # __file__ est une variable spéciale qui contient le chemin du script actuel (main.py)
    current_folder = Path(__file__).parent
    path_constructed = current_folder / DATAS_FOLDER_NAME / HISTORIC_FILE_NAME
    return path_constructed


class File:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def getInfos(self):
        return f"File(name={self.name}, path={self.path})"
    
    def read(self):
        try:
            chemin = self.path
            with open(chemin,"r") as file:
                content = json.load(file)
                return content
        except FileNotFoundError:
            print("Fichier de chemin \"{}\" non trouvé".format(chemin))
            return None
        except json.JSONDecodeError as e:
            print("Erreur lors du décodage JSON : le contenu du fichier n'est pas un JSON valide", e)
            return None
        except Exception as e:
            print("Une erreur s'est produite: {}".format(e))
            return None

    def write(self, content, indentation=4):
        #vérifier si le contenu est bien du JSON
        if not isinstance(content,(list,dict)):
            print("Erreur : le contenu à écrire doit être un objet JSON (list ou dict)")
            return False    
        

        #récupérer les données du fichier
        datas = self.read()

        
        if datas is None:
            datas = []
            
        if not isinstance(datas, list):
            print("Erreur : Le fichier existant ne contient pas une liste JSON.")
            return False
        #ajouter la nouvelle donnée à la liste
        datas.append(content)

        try:
            chemin = self.path
            with open(chemin,"w") as fichier:
                json.dump(datas,fichier, indent=indentation)
                return True
        except PermissionError:
            print("Erreur de permission : impossible d'écrire dans le fichier \"{}\"".format(chemin))
        except TypeError as e:
            print("Erreur de type : {}".format(e))
        except Exception as e:
            print("Une erreur s'est produite: {}".format(e))
        return False
    
    def rechercher(self,terme_de_recherche):
        villes_enregistrees = self.read()

        if villes_enregistrees is None: # self.read() renvoie None si le fichier est vide
            print("Aucune recherche enregistrée dans l'historique.")
            return None
        
        resultats = []
        for ville in villes_enregistrees:
            nom_de_ville = ville.get("localisation","").lower()
            if(terme_de_recherche.lower() in nom_de_ville):
                return ville
        return None

"""
def getFileContent(path):
    try:
        with open(path,"r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("Fichier de chemin \"{}\" non trouvé".format(path))
        return None
    except json.JSONDecodeError as e:
        print("Erreur lors du décodage JSON : le contenu du fichier n'est pas un JSON valide", e)
        return None
    except Exception as e:
        print("Une erreur s'est produite: {}".format(e))
        return None



def wwriteInFile(path, content,indentation=4):
    try:
        with open(path,"w") as fichier:
            json.dump(content,fichier, indent=indentation)
            return True
    except PermissionError:
        print("Erreur de permission : impossible d'écrire dans le fichier \"{}\"".format(path))
    except TypeError as e:
        print("Erreur de type : {}".format(e))
    except Exception as e:
        print("Une erreur s'est produite: {}".format(e))
    return False
        """