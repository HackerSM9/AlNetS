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
elif choice == "3":
    os.system("clear")
    banner.banner()
    dns = input("Enter DNS (URL/IP Add): ")
    os.system("nmap {}".format(dns))
elif choice == "4":
    os.system("clear")
    banner.banner()
    ping = input("Enter URL/IP Address to Ping: ")
    os.system("nmap -sP {}".format(ping))
elif choice == "9":
    os.system("termux-open-url https://github.com/HackerSM9/ip-tracker")
elif choice == "x":
    os.system("termux-open-url https://github.com/HackerSM9/")
elif choice == "off" or "OFF":
    sys.exit()
else:
    print(":( No Option from Above List. ")