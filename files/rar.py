import rarfile
import os,sys
from tqdm import tqdm


def testingPWD(fn,password):
    try:
        rar = rarfile.RarFile(fn)
        try:
           rar.extractall(pwd=password)
           return 1
        except:
            return -1
    except:
        return 0

wordlist = input("Enter your wordlist: ")
protected_file = input("Enter your RAR protected file: ")

passwords = [line.strip() for line in open(wordlist)]

if not os.path.isfile(protected_file):
    print(f"\033[0;31m[+]\033[0m File Not Found {protected_file}")
    sys.exit()

if not os.path.isfile(wordlist):
    print(f"\033[0;31m[+]\033[0m Wordlist Not Found: {wordlist}")
    sys.exit()

print("")

file = open(wordlist,"r")
for password in tqdm(passwords, desc="\033[0;31m[+]\033[0m Trying Password..."):
    replace=password.strip().replace('\r\n','').replace('\n','')
    strip = testingPWD(protected_file,replace)
    if strip ==1:
        print(f"\033[0;32m[!]\033[0m Password Found: {replace}")
        sys.exit()
    elif strip ==-1:
        print(f"\033[0;31m[+]\033[0m Not Found: {replace}")
    else:
        sys.exit()