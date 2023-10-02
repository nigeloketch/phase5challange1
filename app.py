# Import necessary modules and classes from Flask and related extensions.
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import *
from flask_restful import Api, Resource


# Create a Flask application instance.
app = Flask(__name__)

# Configure the database URI and disable track modifications.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the migration extension with the Flask app.
migrate = Migrate(app, db)

# Initialize the database with the Flask app.
db.init_app(app)

# Create an instance of the Flask-RESTful API.
api = Api(app)

# Define a route to get all restaurants.
class GetRestaurant(Resource):
    def get(self):
        #  Query all restaurants from the database.
         restaurants = Restaurant.query.all()
         restaurant_list = []

        # Create a list of restaurant data.
         for res in restaurants:
             res_data = {
                 "id": res.id,
                 "name": res.restName,
                 "address": res.address
             }
             restaurant_list.append(res_data)

    #   Return the list of restaurants as JSON.
         return jsonify(restaurant_list)

# Add the GetRestaurant resource to the API and define its route.
api.add_resource(GetRestaurant, "/restaurants")

# Define a resource to get a restaurant by its ID and delete it.
class GetRestaurantbyID(Resource):
    def get(self, id):
        # Query a restaurant by its ID from the database.
        restaurant = Restaurant.query.get(id)
        res_data = {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        }

        # Return the restaurant data as JSON.
        return jsonify(res_data)

    def delete(self, id):
        # Query and delete a restaurant by its ID from the database.
        restaurant = Restaurant.query.get(id)
        db.session.delete(restaurant)
        db.session.commit()

        # Return an empty response.
        return "{}"

# Define a resource to get all pizzas.
class PizzaRoute(Resource):
    def get(self):
        # Query all pizzas from the database.
        list_of_pizzas = Pizza.query.all()
        pizza_list = []

        # Create a list of pizza data.
        for pizza in list_of_pizzas:
            pizza_data = {
                "id": pizza.id,
                "name": pizza.name,
                "price": pizza.address,  # Note: This should likely be "price" instead of "address."
                "ingredients": pizza.ingredients
            }
            pizza_list.append(pizza_data)

        # Return the list of pizzas as JSON.
        return jsonify(pizza_list)

# Add the Pizza resource to the API and define its route.
api.add_resource(PizzaRoute, "/pizzas")

# Define a resource to associate a pizza with a restaurant.
class RestaurantPizza(Resource):
    def post(self):
        # Create a new RestaurantPizza object based on the request data.
        new_RestaurantPizza = Restaurant_Pizza(
            restaurant_id= request.form.get("restaurant_id"),
            pizza_id=request.form.get("pizza_id"),
            price = request.form.get("price")
        )

        # Add the new RestaurantPizza object to the database.
        db.session.add(new_RestaurantPizza)
        db.session.commit()

        # Retrieve the added pizza's information from the database.
        pizza = Pizza.query.filter(Pizza.id == request.form.get('pizza_id')).first()

        # Create a dictionary with pizza information.
        pizza_data = {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        }

        # Return the pizza data as JSON with a 201 status code (resource created).
        return jsonify(pizza_data), 201

# Add the RestaurantPizza resource to the API and define its route.
api.add_resource(RestaurantPizza, "/restaurant_pizza")

# Run the application if it's the main script.
if __name__ == '__main__':
    # Create the database tables if they don't exist.
    with app.app_context():
        db.create_all()
    
    # Start the Flask application in debug mode.
    app.run(debug=True)