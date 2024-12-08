from flask_login import UserMixin
from . import mongo, login_manager
from bson.objectid import ObjectId

@login_manager.user_loader
def load_user(user_id):
    user_data = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if user_data:
        return User(
            fullname=user_data['fullname'],
            email=user_data['email'],
            password_hash=user_data['password_hash'],
            high_score=user_data['high_score'],
            id=str(user_data['_id']),
        )
    return None

class User(UserMixin):
    def __init__(self, fullname, email, password_hash, high_score, id=None):
        self.id = id
        self.fullname = fullname
        self.email = email
        self.password_hash = password_hash
        self.high_score = high_score

    @staticmethod
    def create_user(data):
        result = mongo.db.users.insert_one(data)
        return str(result.inserted_id)

class Question:
    def __init__(self, text, answers, correct_answer):
        self.text = text
        self.answers = answers
        self.correct_answer = correct_answer

    @staticmethod
    def create_question(data):
        mongo.db.questions.insert_one(data)