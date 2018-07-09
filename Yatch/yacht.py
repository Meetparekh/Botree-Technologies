# Score categories
# Change the values as you see fit
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11



def score(dice, category):

    if category==1:
       return dice.count(1)*1

    elif category==2:
        return dice.count(2)*2

    elif category==3:
        return dice.count(3)*3

    elif category==4:
        return dice.count(4)*4

    elif category==5:
        return dice.count(5)*5

    elif category==6:
        return dice.count(6)*6

    elif category==11:
        sum = 0
        for i in dice:
            sum=sum+i
        return sum

    elif category==9:
        s=set(dice)
        if len(s)==5:
            if 1 in s and 6 not in s:
                for i in dice:
                    return 30
            else:
                return 0

        else:
            return 0


    elif category==10:
        s=set(dice)
        if len(s)==5:
            if 1 not in s and 6 in s:
                for i in dice:
                    return 30
            else:
                return 0
        else:
            return 0

    elif category==8:
        for x in dice:
            if dice.count(x)>=4:
                return  x*4
                break
            else:
                return 0

    elif category==7:
        for i in dice:
            if dice.count(i)>3:
                return 0
            else:
                continue

        s = set(dice)
        if len(s) == 2:
            sum = 0
            for i in dice:
                sum = sum + i

            return sum

        else:
            return  0

    elif category==50:
        s=set(dice)
        if len(s)==1:
            return  50
        else:
            return  0











