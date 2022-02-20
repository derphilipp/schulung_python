import subprocess

command = subprocess.run(["python","./examples/process/wait_and_print.py"])
print("The exit code was: %d" % command.returncode)
print("ok")