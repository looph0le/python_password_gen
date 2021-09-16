import random 

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"

upper, lower, nums, syms = True, True, True,True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits

print("---Welcome to python password generator---")
print("Enter the length of your password:")
le = input(">> ")
print("Enter how many passwords you want to fetch:")
am = input(">> ")
length = int(le) # 10 elements in a single password
amount = int(am)
print("\n")
print("Your passwords are successfully fetched:\n")

for x  in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
