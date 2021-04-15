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
        sql = "INSERT INTO userDM_new (userID, firstName, lastName, address, username, password, cityID) VALUES (%d, %s, %s, %s, %s, %s, %d)"
        val = (int(self.userID), self.firstName, self.lastName, self.address,self.username, self.password, int(self.cityID))
        cursor.execute(sql, val)



        i = 0
        while i < len(self.strengthIDs):
            s_id = self.strengthIDs[i]
            sql = "INSERT INTO userStrength_new (userID, strengthID) VALUES (%d, %d)"
            val = (int(self.userID), int(s_id))
            cursor.execute(sql, val)
            i = i + 1
        db.close()

