def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    number_of_words = count_words(text)
    print(number_of_words)

def count_words(s):
    s = s.split()
    return len(s)

def get_text(path):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return(file_contents)
main()