import os, random
import time, sys, socket
from colorama import Fore, Style, init

RED = Fore.LIGHTRED_EX + Style.BRIGHT
BLUE = Fore.LIGHTBLUE_EX + Style.BRIGHT
CYAN = Fore.LIGHTCYAN_EX + Style.BRIGHT
WHITE = Fore.LIGHTWHITE_EX + Style.BRIGHT
GREEN = Fore.LIGHTGREEN_EX + Style.BRIGHT
YELLOW = Fore.LIGHTYELLOW_EX + Style.BRIGHT
MAGENTA = Fore.LIGHTMAGENTA_EX + Style.BRIGHT

os.system("")
init(autoreset=True)

def con(dom):
	try:
		data = socket.gethostbyname(dom)
		with open('ips_list.txt', 'a', encoding='utf-8') as f:
			save = open('ips_list.txt', 'r', encoding='utf-8').read()
			if data not in save:
				print(f'{WHITE}Get IP: {CYAN}{data}')
				f.write(f'{data}\n')
			f.close()
	except KeyboardInterrupt:
		sys.exit(f'{RED}\n\nShutdown Button Detected\nFinishing Program...!!!!\n')
	except (ConnectionAbortedError, ConnectionError, ConnectionResetError):
		sys.exit(f'{RED}\n\nCheck Your Connection And Try Again\nShutdown Program...!!!!\n')
	except (socket.gaierror, UnicodeDecodeError):
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
                                                    

Domain To Ip Converter
Contact For More Information.\n
Site	: https://franzcassano.github.io
Telegram: https://t.me/FranzOnly
Channel : https://t.me/priv8franz
Whatsapp: https://wa.me/message/ELB7F57QS6DUC1\n''')
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