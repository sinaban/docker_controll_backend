import subprocess
from subprocess import PIPE

def run_command(command):


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

command = ["docker","run" , "hello-world"]
docker_run = "docker run --rm -d hello-world".split()
# subprocess.call(docker_run, shell=True)
popen = run_command(command)


