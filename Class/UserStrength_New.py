from Class.DB import DB


class UserStrength_New:
    def __init__(self, userID, StrengthID):
        self.userID = userID
        self.StrengthID = StrengthID

    def save(self):
        db = DB()
        cursor = db.createCursor()
        cursor.execute("INSERT INTO strengthDM_new(strengthID, name) VALUES ("+str(self.userID)+",'"+self.StrengthID+"')")
        db.close()