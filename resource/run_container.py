from flask_restful import Resource, reqparse
import subprocess
from subprocess import PIPE


class RunNewContainer(Resource):
    def run_command(self,command):


        popen = subprocess.Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        popen.wait(500) # wait a little for docker to complete
        error = popen.stderr.readline().decode("utf-8")

        if error != "":
            error = error.replace("\n", "")
            print(f"exception in run command: {error}")
            return {}
        else:
            id = popen.stdout.readline().decode("utf-8")
            id = id.replace("\n", "")
            print(id)

            return id

    def post(self,name):
        command = f'''docker run --rm --network botdocker_botnetwork --name {name} tradingapp/bot'''.split()
        resp = self.run_command(command)
        return {"message" : resp} 
