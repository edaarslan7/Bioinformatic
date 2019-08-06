#string search

str_1 = input("metni giriniz: ")
str_2 = input("aramak istediginiz kelimeyi giriniz: ")
def string_search(string,string_1):
    n = len(string_1) #kisa listenin uzunlugu
    a = len(string)  #uzun listenin uzunlugu
    t = False
    kacTane = 0
    s = 0
    p=0

    for i in range(n-1,a):  #kucuk stringin son el alindigi icin boyutu kadar=n-1 , uzun stringin boyu=a
        s = n-2 #kisa olanin eleman kontrolu icin
        p=p+1
        if(string[i] == string_1[n-1]):
            for b in range(i-1,i-n,-1): #uzun olanin elemanlarini dolasicak kisa olanin boyu kadar
                p=p+1
                if(string[b] == string_1[s]):
                    s-=1
                else:
                    break
        if(s==-1):
            kacTane += 1
    if(kacTane != 0):
        t = True
    return(t,kacTane,p)

print(string_search(str_1,str_2))
