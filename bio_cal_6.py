def frequencies(str1, k):
    a = 0
    liste=[]
    count=[]

    while(k<=len(str1)):
        for i in range(a,k):
            str2=str1[a:k]
        a+=1
        k+=1
        liste.append(str2)

    for i in liste:
        count.append(liste.count(i))
    return count,liste
    
str1='actgactcccacccc'
frequencies(str1,3)
