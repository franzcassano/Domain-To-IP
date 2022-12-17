import os, random
import time, sys, socket
from colorama import Fore, init
from concurrent.futures import ThreadPoolExecutor

BLUE = Fore.BLUE
RED = Fore.LIGHTRED_EX
CYAN = Fore.LIGHTCYAN_EX
WHITE = Fore.LIGHTWHITE_EX
GREEN = Fore.LIGHTGREEN_EX
YELLOW = Fore.LIGHTYELLOW_EX
MAGENTA = Fore.LIGHTMAGENTA_EX

os.system("")
init(autoreset=True)

def con(dom):
	try:
		data = socket.gethostbyname(dom)
		with open('ips_list.txt', 'a') as f:
			save = open('ips_list.txt', 'r').read()
			if data not in save:
				print(f'{WHITE}Get IP: {CYAN}{data}')
				f.write(f'{data}\n')
			f.close()
	except KeyboardInterrupt:
		sys.exit(f'{RED}\n\nShutdown Button Detected\nFinishing Program...!!!!\n')
	except (ConnectionAbortedError, ConnectionError, ConnectionResetError):
		sys.exit(f'{RED}\n\nCheck Your Connection And Try Again\nShutdown Program...!!!!\n')
	except socket.gaierror:
		print(f'{WHITE}Dead Domain: {RED}{dom}')
	else:
		pass

def main():
	color = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, BLUE]
	ban =  ('''
   _______    _____                      __         
  /  _/ _ \  / ___/__  ___ _  _____ ____/ /____ ____
 _/ // ___/ / /__/ _ \/ _ \ |/ / -_) __/ __/ -_) __/
/___/_/     \___/\___/_//_/___/\__/_/  \__/\__/_/   
                                                    

Domain To Ip Converter With Threading System
Contact For More Information.
Telegram: https://t.me/franzlc7
Whatsapp: https://wa.me/message/XCDZUUHYN6G5M1''')
	ran = random.choice(color)
	time.sleep(0.1)
	if(os.name == 'posix'):
		os.system('clear')
	else:
		os.system('cls')
	print(ran+ban)
	try:
		do = input(f'{CYAN}List Domain  :')
		proc = open(do, 'r').read().replace('http://', '').replace('https://', '').splitlines()
		for i in proc:
			con(i)
	except KeyboardInterrupt:
		sys.exit(f'{RED}\n\nShutdown Button Detected\nFinishing Program...!!!!\n')
	except (ConnectionAbortedError, ConnectionError, ConnectionResetError):
		sys.exit(f'{RED}\n\nCheck Your Connection And Try Again\nShutdown Program...!!!!\n')
	except FileNotFoundError:
		print(f'{RED}Please Input Valid File!!!')
	else:
		pass

if __name__ == '__main__':
	main()