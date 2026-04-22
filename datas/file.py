import json

historicFileUrl = "historic.json"

def  writeJSONInFile(file,data):
    with open(file,"w",encoding="utf-8") as fichier:
        #fichier.write(data)
        json.dump(data,fichier,indent=4)


def readFromFile(file):
    with open(file,"r",encoding="utf-8") as fichier:
        return fichier.read()
    return ""

#phase de test
writeJSONInFile(historicFileUrl,{"name":"toto","age":12})
print(readFromFile(historicFileUrl))

class FileManager:
    def __init__(self,url):
        self.url = url

    def readDatas(self):
        pass