import Class
db = Class.DB.DB()
cursor = db.createCursor()
cursor.execute("""
      select * from cityDM_old
   """)
result = cursor.fetchall()
print(result)