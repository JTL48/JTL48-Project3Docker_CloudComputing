import os
import re
from collections import Counter
import socket

def read_text_file_list():
    # Get a list of all text files in /home/data
    file_list = [f for f in os.listdir('/home/data') if f.endswith('.txt')]
    grand_total = 0
    word_counts = {}
    top_common = {}
    for file in file_list:
        # Read each text file in /home/data
        with open(f'/home/data/{file}', 'r') as f:
            file_content = f.read()
            
            # To mimic Microsoft Word's word counting process
            # Loop through each character in file_content
            # If alphanumeric or space don't change
            # If \u2014 or em dash change to space
            # If any other special character (',;:) change to nothing
            file_content = ''.join(c if c.isalnum() or c.isspace() else ' ' if c == '\u2014' '' else '' for c in file_content)
            
            #Make each word lowercase and split by space
            word_list = file_content.lower().split()
            
            # Count the number of words in each file
            word_counts[file] = len(word_list)
            grand_total += len(word_list)
            
            if(file == "IF.txt"):
                # Get the 3 most common words in IF.txt
                top_common[file] = Counter(word_list).most_common(3)
    return file_list, word_counts, grand_total, top_common

def get_ip_address():
    # Get the IP address of your machine
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address
	
def write_to_file(file_list, word_counts, grand_total, top_common, ip_address):
    # Write the results to a text file
    with open('/home/output/result.txt', 'w') as f:
        f.write('Text files in /home/data:\n')
        for file in file_list:
            f.write(f'- {file}\n')
        f.write('\n')
        f.write('Total number of words in each file:\n')
        for file, count in word_counts.items():
            f.write(f'- {file}: {count} words\n')
        f.write('\n')
        f.write(f'Grand total: {grand_total} words\n')
        f.write('\n')
        f.write(f'Top 3 words in IF.txt:\n')
        for file, words in top_common.items():
            for word, count in words:
                f.write(f'- {word}: {count} times\n')
        f.write('\n')
        f.write(f'IP address: {ip_address}\n')

# Call each function:

file_list, word_counts, grand_total, top_common = read_text_file_list()
ip_address = get_ip_address()
write_to_file(file_list, word_counts, grand_total, top_common, ip_address)