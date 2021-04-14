from Class.DB import DB


class User_New:
    def __init__(self, userID, firstName, lastName, address, username, password, cityID, strengthIDs):
        self.userID = userID
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.username = username
        self.password = password
        self.cityID = cityID
        self.strengthIDs = strengthIDs

    def save(self):
        db = DB()
        cursor = db.createCursor()
        cursor.execute(
            "INSERT INTO userDM_new(userID, firstName, lastName, address, username, password, cityID) "
            "VALUES ("+str(self.userID)+",'"+self.firstName+"','"+self.lastName+"','"+self.address+"','"+self.username+"','"+self.password+"',"+str(self.cityID)+")")
        i = 0
        while i < len(self.strengthIDs):
            s_id = self.strengthIDs[i]
            cursor.execute(
                "INSERT INTO userStrength_new(userID, strengthID) "
                "VALUES (" + str(self.userID) + ","+str(s_id)+")")
            i = i + 1
        db.close()

