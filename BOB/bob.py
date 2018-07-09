def hey(phrase):

    p=phrase.strip()

    if p.isupper() and p.endswith('?'):
        return "Calm down, I know what I'm doing!"


    elif p.endswith('?'):
        return 'Sure.'

    elif p.isupper() or p.isdigit():
        return 'Whoa, chill out!'


    elif p is None or p.strip()=='':
        return 'Fine. Be that way!'

    else:
        return 'Whatever.'