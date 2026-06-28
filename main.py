import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
passwordLength = int(input("Şifre uzunluğunu girin:"))
password = ""

for i in range (passwordLength):
    password += random.choice(characters)

print(password)
