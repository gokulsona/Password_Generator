import random
print("\n\nPassword Generator..\t\n")

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y","Z"]

numbers = ["0","1","2","3","4","5","6","7","8","9"]

characters = ["(","!", "@", "$", "%", "^", "&", "*", "+", "#",")"]

nmbr_letters = int(input("Enter Number of Letters : ")) 
nmbr_numbers = int(input("Enter Number of Numbers : "))
nmbr_char = int(input("Enter Number of Characters : "))
#password list
password = []
for i in range(1,nmbr_letters+1):
	rand_letters  = random.choice(letters)
	password.append(rand_letters)
	
for i in range(1,nmbr_numbers+1):
	rand_numbers  = random.choice(numbers)
	password.append(rand_numbers)
	
for i in range(1,nmbr_char+1):
	rand_char = random.choice(characters)
	password.append(rand_char)

random.shuffle(password)
rand_password = ""
for i in password:
	rand_password+=i
print(rand_password)


