from modele.user import User

user = User(0,"","")

def create_user(user_data):
    name = user_data["name"]
    password = user_data["password"]
    return user.create_user(name, password)

def select_user(id):
    return user.select_user(id)

