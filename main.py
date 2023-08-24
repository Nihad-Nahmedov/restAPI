from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Demo(Resource):
    @staticmethod
    def get():
        return jsonify(message="Demo")


api.add_resource(Demo, '/')

if __name__ == '__main__':
    app.run(debug=True)
