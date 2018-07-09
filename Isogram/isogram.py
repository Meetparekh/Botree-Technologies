from string import punctuation

def is_isogram(string):
    s=string.lower()
    letter_list=[]

    for letter in s:

        if letter in letter_list:
            return False

        elif letter in [" ",'-']:
            pass

        else:
            letter_list.append(letter)

    return True
