import hashlib
import crypt
import itertools
from passlib.hash import md5_crypt
from multiprocessing import Pool, cpu_count
import time

salt = '$1$zxHxP/cZ$'

testPass = 'jlvxvc'
# output = crypt.crypt(testPass,salt)
# print(output)

givenPassHash = '$1$zxHxP/cZ$9M9AoyLzpPza73./bvfsJ/'

alphabet = 'abcdefghijklmnopqrstuvwxyz'
passwordLength = range(4, 7)

startTime = time.time()

totalPassCalc = 0

for length in passwordLength: 
    passwords = itertools.product(alphabet, repeat=length)
    for password in passwords: 
        totalPassCalc += 1
        passwordStr = ''.join(password)
        hashedPassToCrack = crypt.crypt(passwordStr, salt)
        print('Pass: ', passwordStr, ' Hashed Test Pass: ', hashedPassToCrack)
        if hashedPassToCrack == givenPassHash: 
            print("Password cracked: ", hashedPassToCrack)
            foundPass = passwordStr
            break
    else:
        print('Pass Not Found')

endTime = time.time() 

totalTime = endTime - startTime

print('Total Pass Calculated: ', totalPassCalc)
print('Total time taken: ', totalTime, ' seconds' )
passPerSec = totalPassCalc / totalTime
print('Passwords Calculated Per Second ', passPerSec)

if foundPass:
    with open("cracked_password.txt", "w") as f:
        f.write(foundPass)
    print("Cracked password has been stored in 'cracked_password.txt'")
else:
    print("Password not found.")
