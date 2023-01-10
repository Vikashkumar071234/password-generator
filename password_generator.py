import random
letters=["a","b","c","d","e","f",'g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z'
    ,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R']
numbers=[0,1,2,3,4,5,6,7,8,9]
symbols=["!",'@','#','$','%','^','&','*','(',')','_']
print("Welcome to password generator")
number_letters=int(input("How many letters you want be in your password?\n"))
number_numbers=int(input("How many numbers you want to be in your password?\n"))
number_symbols=int(input("How many symbols you want to be in your password?\n"))

password=""
for lett in range(1,number_letters+1):
    a=random.choice(letters)
    password=password+a

for lette in range(1,number_numbers+1):
    b=random.choice(letters)
    password=password+b


for lettere in range(1,number_symbols+1):
    c=random.choice(symbols)
    password=password+c

sum_numbers=number_letters+number_symbols+number_numbers

for s in range(1,sum_numbers):
    d=random.choice(password)
    password=password+d
print(password)


