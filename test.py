import hashlib
import itertools
from passlib.hash import md5_crypt
from multiprocessing import Pool, cpu_count

salt = 'zxHxP/cZ'
input = 'overfl'
output = md5_crypt.using(salt=salt).hash(input)
print(output)

givenPassHash = '$1$zxHxP/cZ$9M9AoyLzpPza73./bvfsJ/'

alphabet = 'abcdefghijklmnopqrstuvwxyz'
passwordLength = range(6, 7)

for length in passwordLength: 
    passwords = itertools.product(alphabet, repeat=length)
    for password in passwords: 
        passwordStr = ''.join(password)
        hashedPassToCrack = md5_crypt.using(salt=salt).hash(passwordStr)
        print('Pass: ', passwordStr, ' Hashed Test Pass: ', hashedPassToCrack, ' Given Pass Hash: ', givenPassHash)
        if hashedPassToCrack == givenPassHash: 
            print("Password cracked: ", hashedPassToCrack)
            break
    else:
        print('Pass Not Found')