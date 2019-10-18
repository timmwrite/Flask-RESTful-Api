from flask_restful import Resource, reqparse

class  NearestNeighbors(Resource):

    def get(self):
        return {'nearestneighbors' : 'test'}
