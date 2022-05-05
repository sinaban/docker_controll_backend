
from flask import Flask, send_from_directory
from flask_restful import Api

from flask_cors import CORS
from resource.run_container import RunNewContainer,StopContainer,Containers


app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True


api = Api(app)

api.add_resource(RunNewContainer, '/runnew/<string:name>')
api.add_resource(StopContainer, '/stopcontainer/<string:name>')
api.add_resource(Containers, '/containers')
if __name__ == '__main__':


    if app.config['DEBUG']:

        app.run(host="0.0.0.0", port=7001)