from collections import Counter
import re
def normalize_words(text: str) -> list[str]:
    return re.findall(r"\b\w+\b", text.lower())

file_read = 'text.txt'
try:
    with open(file_read, 'r') as file:
        lines = file.readlines()
        total_lines = len(lines)


        all_text = "".join(lines)
        words = normalize_words(all_text)
        total_words = len(words)

        freq = Counter(words)


       
except FileNotFoundError:
    print("error")  

file_result = 'analysis.txt'
with open(file_result, 'w') as file:
    file.write(f"Total number of lines:{total_lines}\n") 
    file.write(f"Total number of lines:{total_words}\n")
    file.write("Word frequency:\n")

    for word, count in freq.items():
        file.write(f"{word}: {count}\n")