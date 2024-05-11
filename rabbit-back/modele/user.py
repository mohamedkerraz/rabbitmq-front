import sqlite3

class User:
    def __init__(self,id,name,password):
        self.id = id
        self.name = name
        self.password = password

    def create_user(self,name,password):
        
        try:
            conn = sqlite3.connect('user.db')

            cursor = conn.cursor()

            cursor.execute('''INSERT INTO users (name, password) VALUES (?, ?)''', (name, password))

            new_id = cursor.lastrowid

            conn.commit()
            conn.close()
            return {
                "code": 201,
                "message": "User created",
                "id": new_id,
                "success": True
            }
        except:
            return {
                "code": 500,
                "message": "Error while creating user",
                "success": False
            }

    def select_user(self,id):

        conn = sqlite3.connect('user.db')

        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM users where id = ?''', (id,))
        rows = cursor.fetchall()
        print(rows)
        return {
            "code": 200,
            "message": "User selectd",
            "user": rows[0],
            "success": True
        }

    def select_all_user(self):

        conn = sqlite3.connect('user.db')

        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM users''')
        rows = cursor.fetchall()
        users = []
        for row in rows:
            users.append(row)
        return {
            "code": 200,
            "message": "Users",
            "user": users,
            "success": True
        }

