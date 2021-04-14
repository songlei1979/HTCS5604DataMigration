import mysql.connector

class DB:
    def __init__(self):
        self.connection = mysql.connector.connect(user='t8jnow42fmp1smpt',
                                                  password='fdavedw769oxw5pd',
                              host='klbcedmmqp7w17ik.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                              database='k2nfay1osz1i59kc')

    def createCursor(self):
        return self.connection.cursor()

    def close(self):
        self.connection.close()