def main():
    #Path to book
    path = "books/frankenstein.txt"
    text = get_text(path)
    #creating new variable cause of keeping the original untouched
    text_lowered = text.lower()
    number_of_words = count_words(text)
    u_char_count = count_unique(text_lowered)
    sorted_dict = sort_dictionary(u_char_count)
    report(path,number_of_words,sorted_dict)

#cheking if character is in aplhabet and returning clean dictionary 
def clean_dictionary(dic):
    clean_dic = {}
    for d in dic:
        if d.isalpha():
            clean_dic[d] = dic[d]
            
    return clean_dic

#sorting dictionary with cleaning up for better performace
def sort_dictionary(dic):
    dic = clean_dictionary(dic)
    #getting dictionary to list
    list = dic.items()
    #swaping places in tuple 
    swapped_list = [(a,b) for b,a in list]
    #sort the list then creating dictionary and return it
    return dict(sorted(swapped_list,reverse=True))

#counting amout of words
def count_words(s):
    s = s.split()
    return len(s)

#Converting file to string
def get_text(path):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return(file_contents)

def count_unique(s):
    character_count = {}
    for char in s:
        if char in character_count:
            character_count[char] =character_count[char] + 1
        else:
            character_count[char] = 1
        
    return character_count

def report(path,number_of_words,u_char_count):
    print(f"--- Begin report of {path} ---")
    print(f"{number_of_words} words found in the document")
    for ch in u_char_count:
        print(f"The {ch} character was found {u_char_count[ch]} times.")
    print("--- End report ---")


main()