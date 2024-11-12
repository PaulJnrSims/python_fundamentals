import random 

# print(random.random())

# print(random.uniform(1,10))

# print(random.randint(1,10))

my_number = 8
computer_number = random.randint(1,50)

while my_number != computer_number:
    print(f"computer picked {computer_number}. You picked{my_number}. These don't match")
    computer_number = random.randint(1,50)


print(f"Computer picked {computer_number}. You picked {my_number} These do match! Well done computer!")
