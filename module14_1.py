import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')
for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'User{i}', f'example{i}@gmail.com', f'{i}0', '1000'))


for i in range(1, 11):
    if not (i-1) % 2:
        cursor.execute('UPDATE Users SET balance = 500 WHERE id = ?', (i,))

for i in range(1, 11):
    if not (i-1) % 3:
        cursor.execute('DELETE FROM Users WHERE id = ?', (i,))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
users = cursor.fetchall()
for user in users:
    print(f"���: {user[0]} | �����: {user[1]} | �������: {user[2]} | ������: {user[3]}")

connection.commit()
connection.close()