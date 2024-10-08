def main():
    path_file_source = input("Please enter the filepath of the desired book: ")
    book_text_string = book_stored(path_file_source)
    num_words = book_word_counter(book_text_string)
    character_counts = book_character_counts(book_text_string)
    abclist = list_of_dict_charCount_pairs(character_counts)
    formated_report_output(abclist, path_file_source, num_words)

def book_stored(book_path):
    '''Takes the file path of where the text file is stored as a user input string and opens
    the file reading it into a string that gets returned if the user input did not encounter 
    an error. If user input is invalid an error message is displayed and the program is exited.'''
    try:
        with open(book_path) as f:
            book_contents = f.read()
    except FileNotFoundError:
        print(f"No such file or directory: {book_path}")
        exit()
    return book_contents

#takes a string containing contents of a book and returns an 
#int representing the amount of words in the book
def book_word_counter(book_text):
    words = book_text.split()
    count = len(words)
    return count

#takes a string and returns a dictionary with key:value pair of character:count
#with the count conveying the characters appearance in the string.
def book_character_counts(book_text):
    character_count = {}
    lc_book_text = book_text.lower()
    for character in lc_book_text:
        if character in character_count:
            character_count[character] += 1 
        else:
            character_count[character] = 1
    return character_count

def list_of_dict_charCount_pairs(book_text):
    list_of_abc_char_counts = []
    for key in book_text:
        if key.isalpha():
            list_of_abc_char_counts.append({'char': key, 'count': book_text[key]})
    return list_of_abc_char_counts

def sort_on(dict):
    return dict['count']

def formated_report_output(list, filepath, wordcount):
    print(f"--- Beginning report on {filepath} ---")
    print(f"\n{wordcount} words found in document!\n")
    list.sort(reverse=True, key=sort_on)
    for value in list:
        #print(value)
        print(f"The '{value['char']}' character was found {value['count']} times")
    print('\n--- End report ---')

main()