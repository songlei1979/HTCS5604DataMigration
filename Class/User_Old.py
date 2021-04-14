from Class.DB import DB


class User_Old:
    def __init__(self, userID):
        db = DB()
        cursor = db.createCursor()
        cursor.execute("select * from userDM_old where userID = " + str(userID) + "")
        userInfo = cursor.fetchall()[0]
        self.userID = userInfo[0]
        self.firstName = userInfo[1]
        self.lastName = userInfo[2]
        self.address = userInfo[3]
        self.cityID = userInfo[4]
        cursor.execute("select strengthID from userStrength_old where userID = " + str(userID) + "")
        self.strengths = []
        result = cursor.fetchall()
        i = 0
        while i < len(result):
            self.strengths.append(result[i][0])
            i = i + 1
        db.close()

user = User_Old(1)
print(user.__dict__)
