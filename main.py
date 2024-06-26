import os,sys
import src.banner as abs

mdl = abs.AlnetsBanners()

red = '\033[1;31m'
dark_red = '\033[1;31m'
green = '\033[0;92m'
yellow = '\033[1;33m'
violet = '\033[1;34m'
cyan = '\033[0;96m'
end = '\033[0m'
question = yellow+'['+dark_red+'?'+yellow+']'+end
tick = yellow+'['+green+'✓'+yellow+']'+end

os.system("clear")
mdl.banner()
mdl.menu()

choice = input(question+f"{cyan} Choose Your Option:{green} ")

while True:
    try:

        if choice == "0":
            os.system("clear")
            mdl.banner()
            os.system("nmap -V")
        elif choice == "1":
            os.system("clear")
            mdl.banner()
            url = input(f"{cyan}Enter URL:{green} ")
            os.system("nmap {}".format(url))
        elif choice == "2":
            os.system("clear")
            mdl.banner()
            ip_add = input(f"{cyan}Enter IP Address:{green} ")
            os.system("nmap {}".format(ip_add))
        elif choice == "3":
            os.system("clear")
            mdl.banner()
            dns = input(f"{cyan}Enter DNS (URL/IP Add):{green} ")
            os.system("nmap {}".format(dns))
        elif choice == "4":
            os.system("clear")
            mdl.banner()
            ping = input(f"{cyan}Enter URL/IP Address to Ping:{green} ")
            os.system("nmap -sP {}".format(ping))
        elif choice == "9":
            os.system("termux-open-url https://github.com/HackerSM9/ip-tracker")
        elif choice == "x":
            os.system("termux-open-url https://github.com/HackerSM9/")
        elif choice == "off":
            break
        elif choice == "":
            print(f"\n{red}No Input :/\n")
        else:
            print(f"\n{red}No Option from Above List :(\n")

    except KeyboardInterrupt as ki:
        print(f"{red}\nError Occurred due to Keyboard Interruption :/")
        break
    except Exception as e:
        print(f"{red}\nAn Error Occured: {e}")
        break
    finally:
        print(f"{cyan}\nProgram Finished.\n")
        break
