import subprocess
import os,sys
import time
import src.banner as abs

os.system("clear")

mdl = abs.AlnetsBanners()


print("Installing Packages and Requirements...")

subprocess.run(["apt","update","-y"], capture_output=True)
subprocess.run(["apt","upgrade","-y"], capture_output=True)
subprocess.run(["apt","update","-y"], capture_output=True)

print("Setup Completed!\nExecuting Program...")

time.sleep(3)

os.system("python main.py")