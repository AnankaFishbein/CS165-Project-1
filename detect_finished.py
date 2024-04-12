import os
import threading

# Function to detect finished files
def detect_finished_files():
    # Define the folder path
    folder_path = 'strings'

    # List to store finished files
    finished_files = []

    # Lock to synchronize access to the finished_files list
    lock = threading.Lock()

    # Function to check if a file is finished
        # Function to check if a file is finished
    def check_file(filename):
        nonlocal finished_files
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)
        
        # Open the file and read the last line
        with open(file_path, 'r') as file:
            last_line = file.readlines()[-1].strip()
        
        # Check if the last line ends with the appropriate string
        expected_ending = filename.split('_')[-1][0] + "z" * 5  # Expected ending of a fully generated file
        if last_line.endswith(expected_ending):
            with lock:
                finished_files.append(filename)
        # Create and start a thread for each file
        threads = []
        for filename in os.listdir(folder_path):
            thread = threading.Thread(target=check_file, args=(filename,))
            thread.start()
            threads.append(thread)

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

        # Print finished files
        for filename in finished_files:
            print(f"File '{filename}' has finished generating.")

if __name__ == "__main__":
    detect_finished_files()