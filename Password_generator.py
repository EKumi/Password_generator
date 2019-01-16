import random
chars='abcdefghijklmnopqrstuvwxyz1234567890'
length=int(input(' What should your password length be:'))
password_number=int(input('How many passwords do you want ?:'))
for p in range(password_number):
    password=''
    for c in range(length):
        password+=random.choice(chars)
    print(password)

