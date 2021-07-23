from main import *

class User(db.Model): #creation of database
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(1000), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))


    def __repr__(self):
        return f"User('{self.email}','{self.name_of_subscription}', '{self.billing_cycle}', {self.cost})" 

class Subscription(db.Model): #creation of database
    id = db.Column(db.Integer, primary_key=True)
    name_of_subscription = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    billing_cycle = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.email}','{self.name_of_subscription}', '{self.billing_cycle}')"