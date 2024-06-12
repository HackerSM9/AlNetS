red = '\033[0;91m'
dark_red = '\033[1;91m'
green = '\033[0;32m'
instance_green = '\033[1;92m'
yellow = '\033[1;33m'
light_yellow = '\033[0;93m'
light_violet = '\033[1;94m'
magenta = '\033[1;95m'#35
pink = '\033[0;35m'#1;95
cyan = '\033[1;96m'

end = '\033[0m'

question = yellow+'['+red+'?'+yellow+']'+end
tick = yellow+'['+green+'✓'+yellow+']'+end

class AlnetsBanners():

  def banner(self):
    print(f"""{magenta}

      __      ___      _____  ___    _______  ___________  ________  
     /""\    |"  |    (\"   \|"  \  /"     "|("     _   ")/"       ) 
    /    \   ||  |    |.\\\   \    |(: ______) )__/  \\\__/(:   \___/  
   /' /\  \  |:  |    |: \.   \\\  | \/    |      \\\_ /    \___  \    
{dark_red}  //  __'  \ ||  |___ |.  \    \. | // ___)_     |.  |     __/  \\\   
 /   /  \\\   \( \_|: \|    \    \ |(:      "|    \\\: |    /" \   :)  
(___/    \___)\_______)\___|\____\) \_______)     \__|   (_______/   
                                                                     
     {pink}<======= {instance_green}All Network Scanner{pink} By {cyan}HackerSM9{pink} | {green}v1.2 {pink}=======> 
                                                  
 {end}  """ )


  def menu(self):
    print(f"""{light_violet}
   0) Check Version 
   1) Scan URL
   2) Scan IP Address
   3) Scan DNS (URL/IP Add)
   4) Ping (URL/IP Add)
   9) Similar Tools
   x) About Author
 {light_yellow}
<== Type {dark_red}'off'{light_yellow} to Exit ==>
   """)