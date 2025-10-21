import re

def is_sentence(text):
    if not isinstance(text, str) or not text.strip():
        return False

    if not text[0].isupper():
        return False

    if not re.search(r'[.!?]$', text):
        return False

    if not re.search(r'\w+', text):
        return False

    return True

def get_sentence():
    user_sentence = input("Enter a sentence: ")
    return user_sentence

def calculate_frequencies(user_sentence):
        user_sentence = user_sentence.replace(",", "")
        user_sentence = user_sentence.replace(".", "")
        divided = user_sentence.lower().split()
        return divided

def sentence_check(user_sentence):
    while (is_sentence(user_sentence) == False):
        print("This does not meet the criteria for a sentence.")
        user_sentence = input("Enter a sentence: ")
    if (is_sentence(user_sentence) == True):
            calculate_frequencies(user_sentence)

def print_frequencies(divided):
    unique = []
    for word in divided:
        if word not in unique:
            unique.append(word)
    for y in unique:
        print(y.title(),"-->",  divided.count(y))


def run():
    text = get_sentence()
    is_sentence(text)
    sentence_check(text)
    divided = calculate_frequencies(text)
    print_frequencies(divided)

run()
