import os
import socket
from collections import Counter

# Path to the data folder inside the container
data_path = '/home/data'

# List all text files in the /home/data folder
text_files = [file for file in os.listdir(data_path) if file.endswith('.txt')]

# Output file path
output_path = '/home/output/result.txt'

# Function to count words in a file
def count_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
    return len(words)

# Function to find top words in a file
def top_words(file_path, n=3):
    with open(file_path, 'r') as file:
        words = file.read().split()
    word_counts = Counter(words)
    return word_counts.most_common(n)

# List all text files in /home/data
print(f"List of text files in {data_path}: {text_files}")

# Count total words in each text file and calculate the grand total
grand_total = 0
file_word_counts = {}  # Dictionary to store word counts for each file
for file in text_files:
    file_path = os.path.join(data_path, file)
    file_word_count = count_words(file_path)
    file_word_counts[file] = file_word_count  # Store individual file word counts
    print(f"Total words in {file}: {file_word_count}")
    grand_total += file_word_count

# Print the grand total to the console
print(f"Grand total words: {grand_total}")

# List the top 3 words in IF.txt with counts
if_txt_path = os.path.join(data_path, 'IF.txt')
top_words_if = top_words(if_txt_path)
print(f"Top 3 words in IF.txt: {top_words_if}")

# Find the IP address of the machine
host_ip = socket.gethostbyname(socket.gethostname())
print(f"IP address of the machine: {host_ip}")

# Write the output to the result.txt file
with open(output_path, 'w') as result_file:
    result_file.write(f"List of text files: {text_files}\n")
    result_file.write(f"Grand total words: {grand_total}\n")

    # Write individual word counts for each file
    for file, count in file_word_counts.items():
        result_file.write(f"Total words in {file}: {count}\n")

    result_file.write(f"Top 3 words in IF.txt: {top_words_if}\n")
    result_file.write(f"IP address of the machine: {host_ip}\n")

print(f"Output written to {output_path}")
