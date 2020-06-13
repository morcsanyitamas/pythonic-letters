word = "Pythonic letters"
def print_letters(word):
    pythonic_word_list = []
    for letter in word:
        pythonic_word_list.append(letter)    
    return pythonic_word_list

def print_letters_comp(word):
	pythonic_word_list = [letter for letter in word]
	
	
