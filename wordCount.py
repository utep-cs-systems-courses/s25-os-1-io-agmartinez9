import sys
import os

if len(sys.argv) != 3:
    print("Please give me an input file and output file!")
    print("Like this: python wordCount.py input.txt output.txt")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    # Read the input file
    file = open(input_file, 'r')
    text = file.read()
    file.close()
    
    # Make everything lowercase
    text = text.lower()
    
    # Handle special cases
    text = text.replace("'s", "")  # Remove possessives
    text = text.replace("--", " ")  # Handle double-dash
    text = text.replace("-", " ")   # Split hyphenated words
    text = text.replace('"', ' ')   # Remove quotes
    
    # Get rid of punctuation
    for punct in [',', '.', '!', '?', ';', ':', '(', ')', '[', ']', '{', '}']:
        text = text.replace(punct, ' ')
    
    # Split into words and clean them
    words = text.split()
    
    # Count the words
    word_count = {}
    for word in words:
        # Skip empty strings and single quotes
        if not word or word == '"' or word == "'":
            continue
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Convert to sorted list and sort alphabetically first
    sorted_words = sorted(word_count.items())
    # Then sort by count in descending order but maintain alphabetical order for ties
    sorted_words = sorted(sorted_words, key=lambda x: x[1], reverse=True)
    
    # Write to output file
    output = open(output_file, 'w')
    for word, count in sorted_words:
        output.write(f"{word} {count}\n")
    output.close()
    
except Exception as e:
    print(f"Oops, something went wrong: {e}")
    sys.exit(1)