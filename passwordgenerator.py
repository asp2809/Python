from random import randint
#to generate a random password, I take a string containing all the possible characters that can be used while making a password
str1="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[{]}\|;:,./<>?`~"
num=int(input("Enter the number of passwords you want to generate:"))
n=int(input("Enter the length of the password you want to generate:"))
p=""

#taking a loop with the limit of num i.e. the number of passwords to create
for i in range(num):
    #generating the password by randomly choosing a letter from the string and 91 is taken as there are a total of 92 characaters in the string
    for j in range(n):
        p+=str1[randint(0,91)]
    print(p)
    p=''