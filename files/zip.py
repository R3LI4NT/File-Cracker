from tqdm import tqdm
import zipfile

wordlist = input("Enter your wordlist: ")
protected_file = input("Enter your ZIP protected file: ")

try:
    zip_file = zipfile.ZipFile(protected_file)
    number_pass = len(list(open(wordlist, "rb")))

except FileNotFoundError:
    print("\n\033[0;31mFile or wordlist not found, exiting...\033[0m")
    exit(0)

print("\n")

with open(wordlist, "rb") as wordlist_file:
    for word in tqdm(wordlist_file, desc="\033[0;31m[+]\033[0m Trying Password...", total=number_pass, unit='word'):
        try:
            zip_file.extractall(pwd=word.strip())

        except Exception as e:
            continue

        else:
            print("\033[0;34m[!]\033[0m Password Found:", word.decode().strip())
            print('Exiting...')
            exit(0)
   
