import mysql.connector
from datetime import datetime

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rishmesh_2009",
    database="quizdb"
)

cursor = con.cursor()

today = datetime.now().date()

query = """
SELECT name, marks, correct_answers
FROM leaderboard
WHERE DATE(attempt_time) = %s
ORDER BY marks DESC
"""

cursor.execute(query, (today,))

result = cursor.fetchall()

print("\n===== TODAY'S LEADERBOARD =====\n")

rank = 1

for row in result:
    print(f"{rank}. {row[0]}  |  Marks: {row[1]}  |  Correct Answers: {row[2]}")
    rank += 1