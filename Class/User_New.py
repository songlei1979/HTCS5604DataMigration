from Class.DB import DB


class User_New:
    def __init__(self, userID, firstName, lastName, address, username, password, cityID):
        self.userID = userID
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.username = username
        self.password = password
        self.cityID = cityID

    def save(self):
        db = DB()
        cursor = db.createCursor()
        cursor.execute(
            "INSERT INTO userDM_new(userID, firstName, lastName, address, username, password, cityID) "
            "VALUES ("+str(self.userID)+",'"+self.firstName+"','"+self.lastName+"','"+self.address+"','"+self.username+"','"+self.password+"',"+str(self.cityID)+")")
        db.close()

