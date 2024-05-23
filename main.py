import os,sys
from src import banner

os.system("clear")
banner.banner()
banner.menu()

choice = input("Choose Your Option: ")

if choice == "0":
    os.system("clear")
    banner.banner()
    os.system("nmap -V")
elif choice == "1":
    os.system("clear")
    banner.banner()
    url = input("Enter URL: ")
    os.system("nmap {}".format(url))
elif choice == "2":
    os.system("clear")
    banner.banner()
    ip_add = input("Enter IP Address: ")
    os.system("nmap {}".format(ip_add))