#!/bin/python3


### HEADERS ###

'''

A quick script to make datenight decisions for us so we stop defaulting to the path of least resistance.

Take a list of potential productive --relationship building-- activities, and randomly select one. Come datenight just dot slash and go.


'''

### END HEADERS ###


### IMPORTS ###


from time import sleep
import os, random, argparse, errno, sys


### END IMPORTS ###


### GLOBALS AND ENVIRONMENT ###


help = '''

Usage: ./dateNight.py [-s | -a | -r | -c]

	Please note: Only a single option at a time is accepted

-s, --show :: ./dateNight.py -s

-a, --add :: ./dateNight.py -a 'dance party, board game, special cuddle time'

-r, --remove :: ./dateNight.py -r 'monopoly, make cookies, plan a trip'

-c, --choose :: ./dateNight.py -c

-h, --help :: Show this display

'''

# build argument parser

parser = argparse.ArgumentParser(add_help=False)

parser.add_argument('-s', '--show', action='store_true')
parser.add_argument('-a', '--add', type=str)
parser.add_argument('-r', '--remove', type=str)
parser.add_argument('-c', '--choose', action='store_true')
parser.add_argument('-h', '--help', action='store_true')

args = parser.parse_args()

add,rem,show,choose = False,False,False,False

contents, the_list = [], []


# check how many options were passed, don't accept more than one

arNum = 0
if args.show is True:
	show = True
	arNum += 1
if args.add is not None:
	add = True
	contents = args.add
	arNum += 1
if args.remove is not None:
	rem = True
	contents = args.remove
	arNum += 1
if args.choose is True:
	choose = True
	arNum += 1
if args.help is True:
	print(help)
	exit()
if arNum > 1 or arNum < 1:
	print(help)
	exit()


### END GLOBALS AND ENVIRONMENT ###


### PRIMARY UTILITIES ###


def printer(string):

	# tool for printing strings letter by letter, for aesthetic purposes
	# margins will follow those of the multi-line string
	text = string
	my_list = []
	for letter in text:
		my_list.append(letter)
		show_list = ''.join(my_list)
		sleep(0.07)  #DEFAULT 0.04
		os.system('clear')
		print(show_list)

def add_it(contents):

	# take string from input and separate into list items
	contents = list(contents.replace(', ',',').split(','))
	for item in contents:
		the_list.append(item)
		
	# erase list-on-disk and recreate with updated list		
	dlist = open('list_dateNight.txt','w')
	for item in the_list:
		dlist.write(str(item) + '\n')
	dlist.close()
	
	
def remove_it(contents):

	# take string from input and separate into list items
	contents = list(contents.replace(', ',',').split(','))

	# if any of the passed items is in current list, remove it
	for item in contents:
		for meti in the_list:
			if item == meti:
				the_list.remove(meti)
				
	# erase list-on-disk and recreate with updated list			
	dlist = open('list_dateNight.txt','w')
	for item in the_list:
		dlist.write(str(item) + '\n')
	dlist.close()
	
	
def show_it():

	# if list has items, print them, else don't
	if len(the_list) > 0:
		for item in the_list:
			print(f'\n{item}')
		print('\n')
	else:
		print('\nNothing to show.\n')
		print(help)

def choose_it():

	# if list has items, pick a random number and display the associated list item
	if len(the_list) > 0:
		num = len(the_list) - 1
		ran = random.randint(0, num)
		selection = the_list[ran]
		os.system('clear')
		print('''\n\n\n
	
	
_________________________________________________________
                             _     _                     
        /                    /|   /    ,         /       
----__-/----__--_/_----__---/-| -/---------__---/__--_/_-
  /   /   /   ) /    /___) /  | /    /   /   ) /   ) /   
_(___/___(___(_(_ __(___ _/___|/____/___(___/_/___/_(_ __
                                           /             
_______________________________________(__/________      
                    ____     ____      /   _  _          
    /              /    /    /    )   /    | /           
---/__-----------------/----/___ /---/-----|-----|/      
  /   ) /   /         /    /    |   /     /|     |       
_(___/_(___/_________/____/_____|__o_____/_|____/|_      
          /                                    /         
      (_ /                                              
		\n''')
		
		sleep(3)
		
		printer(f'''

	Tonight is the night for fun! Tonight is the night for dating!
	
	
		Tonight is the night for:
	

				{selection}!
	
		\n\n''')

	else:
		print('\nNothing to choose.\n')
		print(help)
		

### END PRIMARY UTILITIES ###
		
		
### MAIN EXECUTION SEQUENCE ###	


# confirm database file exists, if not build one
# take everything from the file and copy into pseudo-RAM 'the_list'

if os.path.exists('./list_dateNight.txt'):
	dlist = open('list_dateNight.txt','r')
	for item in dlist.readlines():
		the_list.append(item.strip('\n'))
else:

	dlist = open('list_dateNight.txt','x')
	dlist.close()
	
	
# do what the user asks

if add:
	add_it(contents)
	show_it()

if rem:
	remove_it(contents)
	show_it()

if args.show:
	show_it()

if args.choose:
	choose_it()


### END MAIN EXECUTION SEQUENCE ###


### FOOTERS ###


'''
CITATIONS

1) https://pynative.com/python-delete-lines-from-file/

2) https://stackoverflow.com/questions/18839957/argparseargumenterror-argument-h-help-conflicting-option-strings-h

'''


### END FOOTERS ###

