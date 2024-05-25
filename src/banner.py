red = '\033[0;91m'
dark_red = '\033[1;91m'
green = '\033[1;32m'
yellow = '\033[1;33m'
light_violet = '\033[1;94m'
magenta = '\033[0;35m'
end = '\033[0m'
question = yellow+'['+red+'?'+yellow+']'+end
tick = yellow+'['+green+'✓'+yellow+']'+end

def banner():
    print(f"""{magenta}

      __      ___      _____  ___    _______  ___________  ________  
     /""\    |"  |    (\"   \|"  \  /"     "|("     _   ")/"       ) 
    /    \   ||  |    |.\\\   \    |(: ______) )__/  \\\__/(:   \___/  
   /' /\  \  |:  |    |: \.   \\\  | \/    |      \\\_ /    \___  \    
{red}  //  __'  \ ||  |___ |.  \    \. | // ___)_     |.  |     __/  \\\   
 /   /  \\\   \( \_|:  \|    \    \ |(:      "|   \\\: |    /" \   :)  
(___/    \___)\_______)\___|\____\) \_______)     \__|   (_______/   
                                                                     
{end}
                                                  
   """ )


def menu():
    print(f"""{light_violet}
   0) Check Version 
   1) Scan URL
   2) Scan IP Address
   3) Scan DNS (URL/IP Add)
   4) Ping (URL/IP Add)
   9) Similar Tools
   x) About Author
 {yellow}
<== Type {dark_red}'off'{yellow} to Exit ==>
   """)