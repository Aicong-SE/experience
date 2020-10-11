def function(lis):
    if not lis:
        return
    lis.sort()
    a1=[lis[0]]
    a2=[]
    a3=[]
    num = 0
    res = []
    print(lis)
    for i in range(1,len(lis)):
        if lis[i] == lis[i-1]:
            num += 1
        elif lis[i] == lis[i-1]+1:
            num = 0
        else:
            num = 0
            a1 = []
            a2 = []
            a3 = []

        if num == 0:
            a1.append(lis[i])
        elif num == 1:
            a2.extend([lis[i],lis[i]])
        elif num == 2:
            a3.extend([lis[i],lis[i],lis[i]])

        p = a1 if len(a1) > len(a2) else a2
        p = p if len(p) > len(a3) else a3
        res = p if len(p) > len(res) else res

    if 1 in lis and 1 not in a1 and 13 in a1:
        a1.append(1)

    return a1 if len(a1) > len(res) else res



if __name__ == '__main__':
    print(function([1,1,1,2,2,6,10,13,3,11,12,11,9,8,4,5,3,2]))