def is_pangram(sentence):
    s=set()
    sen=sentence.lower()
    for letter in sen:
        if letter.isalpha():
            s.add(letter)
    if len(s)==26:
        return True
    else:
        return False
