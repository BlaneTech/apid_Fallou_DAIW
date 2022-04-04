
from controller.help import *
from model.database import *
# from model.user import *
from controller.requetes import *
# from view.view import *

connexion= Database()
connexion.connection()

class Controller(Helpers):

    def __init__(self):
        # self.user = User()
        self.database = Database()
        # self.view = View()

    def displays(self,n):
        x = self.sqlRequest(sql[n])
        select = self.database.query(x)
        return select

    def addressProcessing(self):
        d=self.getData(urlApi['user'])
        i=self.insertRequest(sql['address'])

        for line in range(d.__len__()):
            self.addressData  = (d[line]['address']['street'],d[line]['address']['suite'],d[line]['address']['city'],d[line]['address']['zipcode'],d[line]['address']['geo']['lat'],d[line]['address']['geo']['lng'])
            self.database.execute(i,self.addressData)
        self.database.commit()

    def userProcessing(self):
        d=self.getData(urlApi['user'])
        i=self.insertRequest(sql['user'])

        for line in range(d.__len__()):
            self.userData  = (d[line].get('id'),d[line].get('name'),d[line].get('username'),d[line].get('email'),d[line].get('phone'),d[line].get('website'),line+1)
            self.database.execute(i,self.userData)
        self.database.commit()
    
    def companyProcessing(self):
        d=self.getData(urlApi['user'])
        i=self.insertRequest(sql['company'])

        for line in range(d.__len__()):
            self.companyData  = (d[line]['company']['name'],d[line]['company']['catchPhrase'],d[line]['company']['bs'],d[line].get('id') )
            self.database.execute(i,self.companyData)
        self.database.commit()

    def postProcessing(self):
        d=self.getData(urlApi['post'])
        i=self.insertRequest(sql['post'])

        for line in range(d.__len__()):
            self.postData  = (d[line].get('id'),d[line].get('title'),d[line].get('body'),d[line].get('userId') )
            self.database.execute(i,self.postData)
        self.database.commit()

    def commentProcessing(self):
        d=self.getData(urlApi['comment'])
        i=self.insertRequest(sql['comment'])

        for line in range(d.__len__()):
            self.commentData  = (d[line].get('id'),d[line].get('name'),d[line].get('email'),d[line].get('body'),d[line].get('postId') )
            self.database.execute(i,self.commentData)
        self.database.commit()

    def albumProcessing(self):
        d=self.getData(urlApi['album'])
        i=self.insertRequest(sql['album'])

        for line in range(d.__len__()):
            self.albumData  = (d[line].get('id'),d[line].get('title'),d[line].get('userId') )
            self.database.execute(i,self.albumData)
        self.database.commit()

    def photoProcessing(self):
        d=self.getData(urlApi['photo'])
        i=self.insertRequest(sql['photo'])

        for line in range(d.__len__()):
            self.photoData  = (d[line].get('id'),d[line].get('title'),d[line].get('url'),d[line].get('thumbnailUrl'),d[line].get('albumId') )
            self.database.execute(i,self.photoData)
        self.database.commit()

    def todoProcessing(self):
        d=self.getData(urlApi['todo'])
        i=self.insertRequest(sql['todo'])

        for line in range(d.__len__()):
            self.todoData  = (d[line].get('id'),d[line].get('title'),d[line].get('userId') )
            self.database.execute(i,self.todoData)
        self.database.commit()
        
connexion.close()