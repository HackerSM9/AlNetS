import subprocess
import os,sys
import time

print("Installing Packages and Requirements...")

subprocess.run(["apt","update","-y"], capture_output=True)
subprocess.run(["apt","upgrade","-y"], capture_output=True)
subprocess.run(["apt","update","-y"], capture_output=True)

print("Setup Completed!\nExecuting Program...")

time.sleep(3)

os.system("python main.py")