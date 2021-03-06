from flask_restful import Resource, reqparse
import subprocess
from subprocess import PIPE
import json
import asyncio


def run_command_iter(command):
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line 
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, command)  

def run_command(command):


    popen = subprocess.Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    popen.wait(50) # wait a little for docker to complete
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

class RunNewContainer(Resource):

    def post(self,name):
        command = f'''docker run --rm -d --network botdocker_botnetwork --name b{name} tradingapp/bot'''.split()
        resp = run_command(command)
        return {"message" : resp} 

class StopContainer(Resource):


    def post(self,name):
        command = f'''docker stop b{name} '''.split()
        resp = run_command(command)
        return {"message" : resp} 

class Containers(Resource):
    def get(self):
        command = f'''docker ps'''.split()
        resp = run_command_iter(command)
        # for i in resp:
        #     print((i.split(" ")[-1]))
        names ={"container_names":
        [line.split(" ")[-1].replace("\n","") for line in resp]}
        return names 
