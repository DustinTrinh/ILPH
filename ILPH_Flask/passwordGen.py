import bcrypt
from database_queries import *
"""
passwd = 'dustythecutie'
test = passwd.encode('utf-8')

pwd = '280398'
test1 = pwd.encode('utf-8')

salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(test, salt)
aaa = b'$2b$12$dJ1eQ09wiGTOuJPEo28apOfDk32hjWWOQvnplkdOA8c0LdmZXaLty'

print(salt)
print(hashed)
print("Salt and Hash Above")
if bcrypt.checkpw(test1, aaa):
    print("match")
else:
    print("does not match")
    
"""
def hash(password):
    encode = password.encode('utf-8')
    print(encode)
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(encode, salt)
    print(hashed)
    return hashed

def decode(password, hash):
    encodePass = password.encode('utf-8')
    if bcrypt.checkpw(encodePass, hash):
        print("Perfect match")
    else:
        print("DOES NOT match")

a = hash('280398')