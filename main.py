import crypt
import itertools
import string

# Generate all permutations of a 5-digit string made up of lowercase alphabet letters
# Generate the alphabet list from 'a' to 'z'
alphabet = list(string.ascii_lowercase)

# Open a file to write the permutations
with open('5_digit_combo.txt', 'w') as file:
    # Write each permutation to the file
    for permutation in itertools.product(alphabet, repeat=4):
        file.write(''.join(permutation) + '\n')

print("Permutations have been written to permutations.txt")

# Given hash string to test against
given_hash = "$1$hfT7jp2q$HtyOYVTSrJkX3GxpxXJY50"
#pwd = 'abcd'
# Given salt
given_salt = "$1$hfT7jp2q$"

# Open the file containing permutations in read mode
with open('5_digit_combo.txt', 'r') as file:
    # Read each line from the file
    for line in file:
        # Strip newline character
        line = line.strip()
        
        # Hash the string using MD5 with the given salt
        hashed_string = crypt.crypt(line, given_salt)

        print(f"Testing: '{line}' with hash '{hashed_string}'")
        
        # Test if the hashed string matches the given hash
        if hashed_string == given_hash:
            print(f"Found match: '{line}' hashes to '{hashed_string}'")
            break  # Stop iterating if a match is found

print("Search complete.")