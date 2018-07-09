def distance(strand_a, strand_b):
    a=len(strand_a)
    b=len(strand_b)

    if a!=b:
        raise ValueError("Length Does not match")

    else:
        c=0
        list_1=[]
        list_2=[]

        for i in strand_a:
            list_1.append(i)

        for j in strand_b:
            list_2.append(j)

        for k in range(a):
            if list_1[k] == list_2[k]:
                continue
            else:
               c=c+1


        return c
