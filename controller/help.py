from requests import get

class Helpers:

    def __init__(self):
        pass

    def insertRequest(self,sql):
        return sql
    
    def sqlRequest(self,sql):
        return sql
    
    def getData(self,url):
        dataFromApi = get(url)
        return dataFromApi.json()
