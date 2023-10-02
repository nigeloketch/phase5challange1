from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db=SQLAlchemy()
class Pizza(db.Model):
    __tablename__ = 'pizza'

    id = db.Column(db.Integer,primary_key=True) # primary key of the table pizza
    name = db.Column(db.String,nullable=False)  # column for storing names in database
    price = db.Column(db.Integer, nullable=False)   #column to store prices in database
    ingridients = db.Column(db.String, nullable=False)

    restaurantPizza = db.relationship('Restaurant_Pizza', backref='pizza')

class Restaurant(db.Model):
    __tablename__ = 'restaurant'

    id = db.Column(db.Integer,primary_key=True)# primary key of restaurant table
    restName = db.Column(db.String,nullable=False)     # column for storing names in database
    address = db.Column(db.String,nullable=False)

    restaurantPizza = db.relationship("Restaurant_Pizza", backref='restaurant')

class Restaurant_Pizza(db.Model):
    __tablename__ = 'restaurantPizza'


    id = db.Column(db.Integer,primary_key=True)    # primary key of pizzarest
    pizza_id = db.Column(db.Integer,db.ForeignKey(Pizza.id))
    price = db.Column(db.Integer,nullable=False)
    restaurant_id = db.Column(db.Integer,db.ForeignKey('restaurant.id'), nullable=False)

    
    
  


    

