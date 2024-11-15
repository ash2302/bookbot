def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    num_words = get_num_words(text)
    char_count = get_num_chars(text)
    sorted_chars = get_sorted_char_counts(char_count)
    print_report(sorted_chars, num_words)
    

def get_text(path):
    with open(path) as f:
        text = f.read()
        return text
        

def get_num_words(text):
    words = text.split()
    return len(words)
 

def get_num_chars(text):
    lowered_text = text.lower()
    char_count = {}
    for char in lowered_text:
        if char.isalpha():  
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

def get_sorted_char_counts(char_count):
    char_items = list(char_count.items())
    sorted_chars = sorted(char_items, key=lambda item: item[1], reverse = True)

    return sorted_chars

def print_report(sorted_chars, num_words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    
    for char, frequency in sorted_chars:
        print(f"The '{char}' character was found {frequency} times")
    
    print("--- End report ---")

main()


