#pip install requests: LOOK DOCUMENTATION
import requests
import textwrap
import sys

target = str(sys.argv[1]) #Automatizing target. Must be the full URL for directories scan and with a final slash (/). For subdomains, must have a dot (.) before the main domain.

wl = open(r'wordlist.txt')
#You have to type the whole path to the file, or if it is in the same directory, you could just type the file name
wordlist = wl.readlines()

dns = open(r'subdomain.txt')
subdomain = dns.readlines()

print("What do you want to scan?")

choice = int(input("1 = Directories,  \n 2 = Subdomain: "))


if choice == 1:
    for word in wordlist:
        if "http" and "/" not in target:
            r = requests.get(f"https://{target}/{word}")
            print(f"https://{target}/{word}")
            print(r.status_code)
        elif target != {target} + "/":
            r = requests.get(f"{target}/{word}")
            print(f"{target}/{word}")
            print(r.status_code)
        else:
            r = requests.get(target + word)
            print(target + word)
            print(r.status_code)

elif choice == 2:
    for sd in subdomain:
        try:
            if "http" and "/" not in target:
                r = requests.get(f"https://{sd}.{target}")
                print(f"https://{sd}.{target}")
                print(r.status_code)
            elif target != "." + {target}:
                r = requests.get(f"{sd}.{target}")
                print(f"{sd}.{target}")
                print(r.status_code)
            else:
                r = requests.get(sd + target)
                print(sd + target)
                print(r.status_code)
        except:
            print(f"{sd}.{target}")
            print("This subdomain doesn't exist!")
else:
    print("Please, pick a valid choice!")
    
    
    
