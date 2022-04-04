import requests

class User:

    def __init__(self):
        pass
        # self.userId = userId
        # self.name = name
        # self.username = username
        # self.userEmail = userEmail
        # self.userPhone = userPhone
        # self.userWebsite = userWebsite

    def insertToUser(self,sql):
        return sql
    
    def getData(self,url):
        dataFromApi = requests.get(url)
        # print("ok")
        return dataFromApi.json()