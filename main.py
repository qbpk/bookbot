def main():   
    book = book_stored("books/frankenstein.txt")
    num_words = book_word_counter(book)
    character_counts = book_character_counts(book)
    print(book)
    print(num_words)
    print(character_counts)

#takes the file path of where the book is stored as a string
#returns contents of book as a string
def book_stored(book_path):
    with open(book_path) as f:
        book_contents = f.read()
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
    #text_of_characters = list(lc_book_text) --> this was not needed. Redundant!
    for character in lc_book_text:
        if character in character_count:
            character_count[character] += 1 
        else:
            character_count[character] = 1
    return character_count

main()