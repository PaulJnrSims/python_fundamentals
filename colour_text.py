# from colorama import Fore, Back, Style

# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

from datetime import date

# day1 = date.today()
# day2 = date(2000,8,16)
# diff = day1 - day2
# print(diff.days, "days so far!")

def number_of_days(date_1, date_2):
    return(date_2 - date_1).days

date_1 = date(2000, 8, 16)
date_2 = date(2024, 11, 12)
print("I have been alive for", number_of_days(date_1, date_2),"days")