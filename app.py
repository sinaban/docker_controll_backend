from flask import Flask, send_from_directory
from flask_restful import Api

from flask_cors import CORS
from resource.run_container import RunNewContainer


app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True


api = Api(app)

api.add_resource(RunNewContainer, '/runnew/<string:name>')

if __name__ == '__main__':


    if app.config['DEBUG']:

        app.run(port=7001)