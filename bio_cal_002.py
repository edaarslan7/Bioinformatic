def frequent_words(str1):
    a,k=0,3
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
    return (count)

print(frequent_words('actgactcccacccc'))
