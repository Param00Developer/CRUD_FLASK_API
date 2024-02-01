from flask import Flask ,jsonify ,request,make_response
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy


from controller.init_con import Customer,Login
from models import CustomerModel

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Blast_user.db'
app.config["SECRET_KEY"]="1212515662564556561546423"
db = SQLAlchemy(app)

#create database only once



# db.create_all()
api.add_resource(Customer, "/user/<int:cus_id>")
api.add_resource(Login, "/login")
# api.add_resource(login,"/login")
if __name__ == "__main__":
	app.run(debug=True)
