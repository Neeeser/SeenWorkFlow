import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
from User import User
from Project import Project


def load_json_info(root, filename):
    with open(filename, "r") as file:
        file_contents = json.load(file)
    root.set(file_contents)


firebase_address = "seenworkflow_private_key.json"

cred = credentials.Certificate(firebase_address)
firebase_admin.initialize_app(cred, {'databaseURL': "https://seenworkflow-default-rtdb.firebaseio.com/"})
root = db.reference('root')
users = db.reference('root/users')
# load_json_info(users, "users.json")

User("joe", "joe_shmoe", "pass123")
User("andrew", "aneeser", "pp23").save_user()
p = Project("Muni Sma", "andrew")
p.add_user("jim-bob")
print(p.remove_user("andrew"))
