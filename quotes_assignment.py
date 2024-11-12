# import random
# from colorama import Fore, Style, init

# init(autoreset=True)

# motivational_quotes = [
# "Success is not final, failure is not fatal. It is the courage to continue that counts. - Winston Churchill",
# "Dont watch the clock; do what it does. Keep going. - Sam Levenson",
# "The only way to do great work is to love what you do. - Steve Jobs"
# ]
 

# funny_quotes = [
# "A day without laughter is a day wasted. - Charlie Chaplin",
# "The best way to cheer yourself up is to try to cheer somebody else up. - Mark Twain",
# "Dance like no one is watching. Sing like no one is listening. - William W. Purkey",
# ]


# meaningful_quotes = [
# "We are what we repeatedly do. Excellence, then, is not an act, but a habit. - Aristotle",
# "In the middle of difficulty lies opportunity. - Albert Einstein",
# "The only thing necessary for the triumph of evil is for good men to do nothing. - Edmund Burke",
# ]


# def get_random_quote(category):
#     category = random.choice(["motivational", "funny", "meaningful"])
#     if category == ("motivatonal_quotes")
#         quote = random.choice(motivational_quotes)
#     elif category == ("funny"):
#         quote = random.choice(funny_quotes)
#     else:
#         quote = random.choice(meaningful_quotes)

#     return quote

# print("Would you like a random quote")
# print(get_random_quote())












import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Lists of quotes for each category
motivational_quotes = [
"Success is not final, failure is not fatal. It is the courage to continue that counts. - Winston Churchill",
"Dont watch the clock; do what it does. Keep going. - Sam Levenson",
"The only way to do great work is to love what you do. - Steve Jobs"
]

funny_quotes = [
"A day without laughter is a day wasted. - Charlie Chaplin",
"The best way to cheer yourself up is to try to cheer somebody else up. - Mark Twain",
"Dance like no one is watching. Sing like no one is listening. - William W. Purkey",
]

meaningful_quotes = [
"We are what we repeatedly do. Excellence, then, is not an act, but a habit. - Aristotle",
"In the middle of difficulty lies opportunity. - Albert Einstein",
"The only thing necessary for the triumph of evil is for good men to do nothing. - Edmund Burke",
]

# Function to display a random quote from a list with colored output
def get_random_quote(category):
    if category == 'motivational':
        return Fore.BLUE + random.choice(motivational_quotes)
    elif category == 'funny':
        return Fore.YELLOW + random.choice(funny_quotes)
    elif category == 'meaningful':
        return Fore.GREEN + random.choice(meaningful_quotes)
    else:
        return "Invalid category!"

# Function to ask if the user wants another quote or to go back to main menu
def ask_for_another_quote():
    while True:
        response = input("Would you like another quote in this category? (yes/no): ").lower()
        if response == 'yes':
            return True
        elif response == 'no':
            return False
        else:
            print("Please answer with 'yes' or 'no'.")

# Main program logic
def main():
    print("Welcome to the Random Quote Generator!")
    while True:
        # Ask the user to choose a category
        category = input("Would you like a motivational, funny, or meaningful quote? (type 'exit' to quit): ").lower()
        
        if category == 'exit':
            print("Thanks for using the Random Quote Generator. Have a great day!")
            break
        
        if category in ['motivational', 'funny', 'meaningful']:
            # Show a random quote from the selected category
            print("\nHere's your quote:")
            print(get_random_quote(category))
            
            # Ask if the user wants another quote in the same category or go back to the main menu
            if ask_for_another_quote():
                continue  # Give another quote in the same category
            else:
                continue  # Go back to the main menu
        else:
            print("Sorry, that's not a valid category. Please choose 'motivational', 'funny', or 'meaningful'.")

if __name__ == "__main__":
    main()
