import random

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Analyzer(Resource):
    def get(self):
        options = ['approved', 'declined']
        option = random.choice(options)
        return {'result': option}


api.add_resource(Analyzer, '/')

if __name__ == '__main__':
    app.run(debug=True)
