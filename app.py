from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import learn_traffic

app = Flask(__name__)
api = Api(app)


class Traffic(object):
    def __init__(self, cars, trucks, busses):
        self.cars = cars
        self.trucks = trucks
        self.busses = busses

    def to_json(self):
        vehicles = self.cars + self.trucks + self.busses
        return jsonify({
            "cars": self.cars,
            "trucks": self.trucks,
            "busses": self.busses,
            "vehicles": vehicles
        })


class AnalyseTraffic(Resource):
    def post(self):
        try:
            json_data = request.get_json()
            data = json_data["image"]
            cars, trucks, busses = learn_traffic.learn_stuff(data)
            traffic = Traffic(cars, trucks, busses)
            return traffic.to_json()
        except Exception as ex:
            return None


class Index(Resource):
    def get(self):
        return "Hello, world!"


api.add_resource(AnalyseTraffic, '/analyse_traffic')
api.add_resource(Index, '/')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
