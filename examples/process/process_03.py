import subprocess

command_process = subprocess.Popen(["python","./examples/process/wait_and_print.py"])
print("We can do a lot of things, while we wait for the process to finish")
command_process.wait()
print("The exit code was: %d" % command_process.returncode)
print("ok")