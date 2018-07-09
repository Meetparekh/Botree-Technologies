def is_armstrong(number):
    a=len(str(number))
    total=0
    temp=number
    while temp>0:
        digit = temp % 10
        total=total+digit**a
        temp = temp // 10

    if number == total:
        return True

    else:
        return False

