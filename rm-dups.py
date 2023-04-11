import sys

if len(sys.argv) != 2:
    print("Usage: python remove_duplicates.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = 'output.txt'

# Read the input file
with open(input_file, 'r') as file:
    lines = file.readlines()

# Remove duplicates and maintain the order of words
unique_words = []
for line in lines:
    word = line.strip()
    if word not in unique_words:
        unique_words.append(word)

# Join the unique words back into a string with new lines
unique_text = '\n'.join(unique_words)

# Write the output to a new file
with open(output_file, 'w') as file:
    file.write(unique_text)