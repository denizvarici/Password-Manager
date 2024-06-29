import string
import random

number_list = list(map(str, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
lowercase_char_list = list(string.ascii_lowercase)
uppercase_char_list = list(string.ascii_uppercase)
special_char_list = list(string.punctuation)
char_list = number_list + lowercase_char_list + uppercase_char_list + special_char_list
def generate_random_pw(char_count = 10):
    random.shuffle(char_list)
    random_chars = random.sample(char_list,char_count)
    
    random_pw = ''.join(random_chars)
    return random_pw
