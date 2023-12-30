# "Here we use base64 to generate key"
import base64
def key():
    p=input('Enter: ')
    a = p.encode('utf-8')
    # "It convert into encode bytes"
    enc_1 = base64.b64encode(a)
    enc_64 = enc_1.decode('utf-8')
    with open('key.key',"w")as f:
        f.write(enc_64)                        # " The key is save into your system as key.key. "
    print("You'r key is generate , so enjoy the show:>")

key()