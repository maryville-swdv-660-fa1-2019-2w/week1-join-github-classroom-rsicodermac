import n2w as n
from colorama import init, Fore, Back

init()

print ( Back.BLUE+ Fore.YELLOW + 'Enter any number: ')
number = input()
print ( n.convert(number))