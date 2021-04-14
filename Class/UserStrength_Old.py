from Class.DB import DB

class UserStrength_Old:
    def __init__(self, userID):
        self.userID = userID
        db = DB()
        cursor = db.createCursor()
        cursor.execute("select name from userStrength_old where userID = "+userID+"")
        self.StrengthIDs = cursor.fetchall()
        db.close()