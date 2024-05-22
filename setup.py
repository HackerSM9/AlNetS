import os,sys

os.system("apt update ; apt upgrade -y")
os.system("pkg install nmap -y")
os.system("python main.py")