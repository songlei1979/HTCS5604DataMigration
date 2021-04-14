from Class.DB import DB

class UserStrength_Old:
    def __init__(self, userID):
        self.userID = userID
        db = DB()
        cursor = db.createCursor()
        cursor.execute("select name from old where userID = "+userID+"")
        self.StrengthIDs = cursor.fetchall()
        db.close()