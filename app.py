from flask import Flask
from flask_restful import Api
from resources.knn import NearestNeighbors

app = Flask(__name__)

api = Api(app)

api.add_resource(NearestNeighbors, '/knn')

app.run(port=5000)