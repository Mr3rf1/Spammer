from pynput import keyboard
from time import sleep, time
from os import name, system

kb = keyboard.Controller()

class colors: 
	black='\033[30m'
	red='\033[31m'
	green='\033[32m'
	orange='\033[33m'
	blue='\033[34m'
	purple='\033[35m'
	cyan='\033[36m'
	lightgrey='\033[37m'
	darkgrey='\033[90m'
	lightred='\033[91m'
	lightgreen='\033[92m'
	yellow='\033[93m'
	lightblue='\033[94m'
	pink='\033[95m'
	lightcyan='\033[96m'
	reset='\033[0m'

def main():
	if name == 'nt': system('cls')
	else: system('clear')

	print(r'''
  ____                                            
{} / ___| _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
{} \___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
{}  ___) | |_) | (_| | | | | | | | | | | |  __/ |   
{} |____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
{}       |_|    
{}
	github.com/e811-py
	t.me/e811_py
'''.format(colors.green, colors.purple, colors.red, colors.purple, colors.green, colors.reset))

	tcount = input(f' {colors.yellow}[{colors.green}?{colors.yellow}] {colors.reset}How many text do you want to send:{colors.green} ')

	while True:
		try:
			tcount = int(tcount)
			if tcount <= 0:
				tcount = int(input(f' {colors.yellow}[{colors.green}!{colors.yellow}] {colors.red}Please Enter a number bigger then 0:{colors.green} '))
			elif tcount > 0:
				break
		except: tcount = input(f' {colors.yellow}[{colors.green}!{colors.yellow}] {colors.red}Please Enter a number:{colors.green} ')

	count = input(f' {colors.yellow}[{colors.green}?{colors.yellow}] {colors.reset}How many messages do you want to send:{colors.green} ')

	while True:
		try:
			count = int(count)
			if count <= 0:
				count = int(input(f' {colors.yellow}[{colors.green}!{colors.yellow}] {colors.red}Please Enter a number bigger then 0:{colors.green} '))
			elif count > 0:
				break
		except: count = input(f' {colors.yellow}[{colors.green}!{colors.yellow}] {colors.red}Please Enter a number:{colors.green} ')

	texts = []
	for i in range(tcount):
		texts.append(input(f' {colors.yellow}[{colors.green}<{colors.yellow}] {colors.reset}Enter text {i+1}: '))

	print(f' {colors.yellow}[{colors.red}!{colors.yellow}] {colors.reset}Plesae Click on the {colors.red}text box{colors.reset}, after 15 seconds spammer will start.')

	m = 15
	for i in range(15):
		if m<=5:
			print(f'\r {colors.yellow}[{colors.red}!{colors.yellow}] {colors.red}{m} {colors.reset}seconds left.', end='')
		else:
			print(f'\r {colors.yellow}[{colors.red}!{colors.yellow}] {colors.reset}{m} seconds left.', end='')
		m-=1
		sleep(1)
	print(f'\r {colors.yellow}[{colors.red}!{colors.yellow}] {colors.reset}Spamming...', end='')
	ft = time()
	for i in range(int(count/tcount)):
		for text in texts:
			for harf in text:
				kb.press(harf)
				kb.release(harf)
			kb.press(keyboard.Key.enter)
			kb.release(keyboard.Key.enter)
			sleep(0.1)
	print(f'\r {colors.yellow}[{colors.red}!{colors.yellow}] {colors.reset}Spam finished in: {int(time() - ft)} seconds :)')

if __name__=='__main__':
	try: main()
	except KeyboardInterrupt: print(f'\n {colors.yellow}[{colors.red}!{colors.yellow}] {colors.reset}Closed.')