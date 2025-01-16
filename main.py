def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    number_of_words = count_words(text)
    text_lowered = text.lower()
    print(number_of_words)

    count_unique(text_lowered)

def count_words(s):
    s = s.split()
    return len(s)

def get_text(path):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return(file_contents)

def count_unique(s):
    characters = set(s)
    character_count = {}
    for char in s:
        if char in character_count:
            character_count[char] =character_count[char] + 1
        else:
            character_count[char] = 1
        
    print(character_count)
            
main()