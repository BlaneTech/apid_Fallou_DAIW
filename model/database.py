from mysql.connector import connect

class Database:
    config = {
        'host': 'localhost',
        'database': 'JSONPlaceholder',
        'user':'YOUR_USERNAME',
        'password':'YOUR_PASSWORD'
    }

    def __init__(self):
        self.dbConnect = connect(**self.config)
        self.cursor = self.dbConnect.cursor()
    
    def connection(self):
        # if self.dbConnect.is_connected():
        #     print('connexion etablie')
        # else: print('errorr')
        return self.dbConnect

    def curseur(self):
        return self.cursor

    def commit(self):
        self.connection().commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection().close()
    
    def execute(self, req, data=None):
        self.curseur().execute(req,data)
    
    def fetchall(self):
        return self.curseur().fetchall()
    
    def query(self, req, data=None):
        self.curseur().execute(req, data or ())
        return self.fetchall()


# conn = database()
# conn.connection()
