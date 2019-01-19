import random
import math
from random import randint
import tkinter
from tkinter import filedialog
from tkinter import *
import os

def encrypt(pk, plaintext):

    cipher=[(char + pk)  for char in plaintext]
    
    return cipher


def decrypt(pk, ciphertext):
    # Unpack the key into its components
    
    plain = [chr(char - pk)  for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)
if __name__ == '__main__':
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Text files","*.txt"),("jpeg files","*.jpg"),("all files","*.*")))
    path= root.filename
    f = open(root.filename,"rb+")
    print (f)
    txt = f.read()
    print("the file is:")
    print (txt)
    key=int(input("input the shift "))
    e=encrypt(key,txt)
    print(e)
    f.truncate(0)
    
    d=decrypt(key,e)
    #print(d)
    a=d.encode()
    pass1=input("enter password for get decrypt message")
    if (pass1=='134'):
        f.write(a)
    f.close()    
    
    f.close()
    