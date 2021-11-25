from banner.banner import * 

bannerMenu()

option = int(input("\n\033[0;32m=> \033[0m"))

if option == 1:
	os.system("cd files && python3 zip.py")

if option == 2:
	os.system("cd files && python3 rar.py")

elif option == 3:
	os.system("cd files && python3 pdf.py")	

