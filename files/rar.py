import rarfile
import os
import sys
from tqdm import tqdm

def testing_password(fn, password):
    try:
        rar = rarfile.RarFile(fn)
        try:
            rar.extractall(pwd=password)
            return 1
        except rarfile.BadRarFile:
            return -1
    except FileNotFoundError:
        return 0

def main():
    wordlist = input("Enter your wordlist: ")
    protected_file = input("Enter your RAR protected file: ")

    if not os.path.isfile(protected_file):
        print(f"\033[0;31m[+]\033[0m File Not Found {protected_file}")
        sys.exit(1)

    if not os.path.isfile(wordlist):
        print(f"\033[0;31m[+]\033[0m Wordlist Not Found: {wordlist}")
        sys.exit(1)

    print("")
    
    with open(wordlist, "r") as file:
        passwords = [line.strip() for line in file]

    for password in tqdm(passwords, desc="\033[0;31m[+]\033[0m Trying Password..."):
        stripped_password = password.replace('\r\n', '').replace('\n', '')
        result = testing_password(protected_file, stripped_password)
        if result == 1:
            print(f"\033[0;32m[!]\033[0m Password Found: {stripped_password}")
            sys.exit(0)
        elif result == -1:
            print(f"\033[0;31m[+]\033[0m Not Found: {stripped_password}")

if __name__ == "__main__":
    main()
