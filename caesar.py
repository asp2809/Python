#program to encrypt data using Caesar Cipher
str1=input("Enter the string which you want to encode:")            #taking input of the string to be encrypted
n=int(input("Enter the number by which you want to shift it(1-26):"))     #taking input of the number by which user wants to shift each character of the string
if n>26 or n<1:
    print("Invalid Input!!!")
l=list(str1)                                                        #splitting the input string
strf=''
#iterating through the list to shift the characters
for i in l:
    p=ord(i)
    if p<123 and p>96:          #checking whether it is a small letter or a capital letter
        p+=n
        if p>=123:
            p=(p-122)+96        #if the range is above the expected then it is shifted in a cycle such that if p+n>expected range then it starts from the beginning i.e. either 97 or 65
    if p>=65 and p<=90:
        p+=n
        if p>91:
            p=(p-90)+64
    strf+=chr(p)                #concatenating the string for the final answer
print(strf)

   
    