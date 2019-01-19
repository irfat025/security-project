import random
import math
from random import randint
import tkinter
import os
from tkinter import filedialog
from tkinter import *
 
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Text files","*.txt"),("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)
#file1=open(root.filename,"r")

f = open(root.filename,"rb+")
data = list(f.read())
#data=f.read()
dt1=data


print("the file is:")
print (data)

f.close()

#p=random.randrange(2**5)
#q=random.randrange(2**5)
p=17
q=23
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def multiplicative_inverse(a,b):
    
    origA = a
    X = 0
    prevX = 1
    Y = 1
    prevY = 0
    while b != 0:
        temp = b
        quotient = a//b
        b = a%b
        a = temp
        temp = X
        a = prevX - quotient * X
        prevX = temp
        temp = Y
        Y = prevY - quotient * Y
        prevY = temp

    return origA + prevY
  
f=gcd(p,q)
    
while(f!=1):
     p=random.randrange(2**10)
     q=random.randrange(2**10)
     f=gcd(p,q)
    
n=p*q
phi=(p-1)*(q-1)
e=random.randrange(1,phi)
g = gcd(e, phi)
while g != 1:
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    
a=e
b=phi
d = multiplicative_inverse(a,b)
print (p,q,d)
def encrypt(e,n, dt1):
    
    cipher=[((i**e)%n)for i in dt1]
    #Return the array of bytes
    return cipher
def decrypt(d,n, ciphertext):
    

    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [((i ** d) % n) for i in ciphertext]
    return ''.join(plain)

    

h=encrypt(e,n,dt1)

print ("the cipher text is:")
#print(''.join(map(lambda x: str(x), h)))
print(h)   
dec=decrypt(d,n,h)
print(dec)    

    


      
       
       
