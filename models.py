from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db=SQLAlchemy()
class Pizza(db.Model):
    id = db.Column('pizzaId',db.Integer,primary_key=True) # primary key of the table pizza
    name = db.Column("name",db.String())  # column for storing names in database
    price = db.Column("price",db.Float(),default="0")   #column to store prices in database
    ingridients = db.Column("ingridients",db.String)

class Restaurant(db.Model):
    id = db.Column('restaurantID',db.Integer,primary_key=True)# primary key of restaurant table
    restName = db.Column("restName",db.String())     # column for storing names in database
    address = db.column("address",db.String())

class Restaurant_Pizza(db.Model):
    id = db.Column('pizzaRestID',db.Integer,primary_key=True)    # primary key of pizzarest
    Reataurant_id = db.Column("Restaurant_id)",db.String())
    pizza_id = db.Column("Pizza_id",db.Integer,db.ForeignKey(Pizza.id))
    price = db.Column("price",db.Integer)
    restaurant_id = db.column("price",db.Integer)

    restaurant = db.relationship("Restaurant",backref=db.backref("restaurant_pizzas",lazy='dynamic'))
    pizza = db.relationship("pizza",backref=db.backref("pizza_restaurants",lazy='dynamic'))

  


    

