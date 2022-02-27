import subprocess
import time

things_to_do = ["read a book", "fly a kite", "drink some tea", "learn to play the piano","paint a picture", "play retro games"]

command_process = subprocess.Popen(["python","./examples/process/wait_and_print.py"])
print("We can do a lot of things, for example...")
while command_process.poll() is None:
    print(things_to_do.pop())
    time.sleep(1)
print("The exit code was: %d" % command_process.returncode)
print("ok")