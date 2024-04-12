import os
import itertools
import string
import multiprocessing

# Function to generate all permutations of a 6-letter string made up of lowercase alphabet letters
def generate_permutations(start_char, end_char):
    # Generate the alphabet list from 'a' to 'z'
    alphabet = list(string.ascii_lowercase)

    # Create a folder named "strings" if it doesn't exist
    folder_path = 'strings'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Open a file to write the permutations
    file_path = os.path.join(folder_path, f'5_digit_combo_{start_char}.txt')
    with open(file_path, 'a') as file:
        # Write each permutation to the file
        for permutation in itertools.product(alphabet, repeat=6):
            # Check if the permutation starts with the specified character range
            if start_char <= permutation[0] <= end_char:
                file.write(''.join(permutation) + '\n')

    print(f"Permutations starting with {start_char} have been written to {file_path}")

if __name__ == "__main__":
    # Define the number of processes (one for each letter of the alphabet)
    num_processes = 26

    # Create a process for each letter of the alphabet
    processes = []
    for i in range(num_processes):
        start_char = chr(ord('a') + i)
        end_char = chr(ord('a') + i + 1) if i < num_processes - 1 else 'z'
        process = multiprocessing.Process(target=generate_permutations, args=(start_char, end_char))
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    print("Permutation generation complete.")