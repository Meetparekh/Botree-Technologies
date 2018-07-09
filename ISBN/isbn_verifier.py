def verify(isbn):
    total=0
    k=11
    isbn1=isbn.replace('-','')
    length =len(isbn1)

    if length == 10:
        for i in range(length-1):
            if isbn1[i].isdigit() :
                continue
            else:
                return False

        if isbn1[9]=='X':
            total=total+10
            for i in range(length-1):
                for j in reversed(range(2,k,1)):
                    g=int(isbn1[i])*j
                    total=total+g
                    break
                k=k-1

        elif isbn1[9].isalpha():
            return False

        else:
            for i in range(length):
                for j in reversed(range(1,k,1)):
                    g=int(isbn1[i])*j
                    total=total+g
                    break
                k=k-1

        if total%11 ==0:
            return True
        else:
            return False
            
    else:
        return False
