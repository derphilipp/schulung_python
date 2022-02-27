import subprocess

# A command that does not exist
command = subprocess.run(["python", "file_not_found.py"])
print("The exit code was: %d" % command.returncode)
print("I continue running...")


command = subprocess.run(["python", "file_not_found.py"], check=True)
print("The exit code was: %d" % command.returncode)
print("I continue running...")