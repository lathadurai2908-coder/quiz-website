import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rishmesh_2009",
    database="quizdb"
)

cursor = db.cursor()

cursor.execute("DELETE FROM leaderboard")

db.commit()

print("Leaderboard cleared")