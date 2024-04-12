import os
import multiprocessing
import crypt

# Given hash string to test against
given_hash = "9M9AoyLzpPza73./bvfsJ/"
# Given salt
given_salt = "$1$zxHxP/cZ$"

# Function to test hashes for a given range of lines in a file
def test_hashes_for_range(file_name, start_line, end_line, result_queue, stop_event, progress_callback):
    result = None
    lines_processed = 0
    with open(file_name, 'r') as file:
        # Move to the start line
        for _ in range(start_line):
            file.readline()
        
        for line_num in range(start_line, end_line + 1):
            if stop_event.is_set():
                break
            
            line = file.readline().strip()
            # Hash the string using crypt with the given salt
            hashed_string = crypt.crypt(line, given_salt)
            # Test if the hashed string matches the given hash
            if hashed_string == given_hash:
                result = line
                break
            
            lines_processed += 1
            progress_callback(lines_processed / (end_line - start_line + 1) * 100)

    result_queue.put(result)

# Function to split the file into two regions and run two processes
def split_and_run(file_name):
    # Calculate the midpoint
    with open(file_name, 'r') as file:
        total_lines = sum(1 for _ in file)
    midpoint = total_lines // 2

    # Create a queue to communicate results between processes
    result_queue = multiprocessing.Queue()
    # Create an event to stop all processes when a valid password is found
    stop_event = multiprocessing.Event()

    # Define a progress callback function
    def progress_callback(progress):
        with open("result.txt", 'w') as result_file:
            result_file.write(f"Progress: {progress:.2f}%\n")

    # Create processes for each region
    process1 = multiprocessing.Process(target=test_hashes_for_range, args=(file_name, 0, midpoint, result_queue, stop_event, progress_callback))
    process2 = multiprocessing.Process(target=test_hashes_for_range, args=(file_name, midpoint + 1, total_lines, result_queue, stop_event, progress_callback))

    # Start the processes
    process1.start()
    process2.start()

    # Wait for the processes to finish
    process1.join()
    process2.join()

    # Check if a valid password was found
    result = result_queue.get()
    if result:
        with open("result.txt", 'a') as result_file:
            result_file.write(f"Found match: '{result}' hashes to '{given_hash}'\n")
        stop_event.set()  # Set the event to stop all processes

if __name__ == "__main__":
    file_name = "strings/6_digit_13.txt"  # Adjust the path to your input text file
    split_and_run(file_name)
