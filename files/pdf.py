from tqdm import tqdm
import pikepdf
import os,sys

wordlist = input("Enter your wordlist: ")
protected_file = input("Enter your PDF protected file: ")

passwords = [line.strip() for line in open(wordlist)]

if not os.path.isfile(protected_file):
    print(f"\n\033[0;31m[+]\033[0m File Not Found {protected_file}")
    sys.exit()

if not os.path.isfile(wordlist):
    print(f"\033[0;31m[+]\033[0m Wordlist Not Found: {wordlist}")
    sys.exit()

try:
    number_pass = len(list(open(wordlist, "rb")))

except FileNotFoundError as err:
    print("\n\033[0;31m[Error]\033[0m File or wordlist not found, exiting...")
    exit(0)

print("\n")

for password in tqdm(passwords, desc="\033[0;31m[+]\033[0m Trying Password...",total=number_pass):

    try:
        with pikepdf.open(protected_file,password=password) as pdf:
            print("\033[0;32m[!]\033[0m Password Found",password)
            print('Exiting...')
            exit(0)

    except pikepdf._qpdf.PasswordError as err:
    	continue       
