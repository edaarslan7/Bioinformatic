def search_with_error(str_1,str_2,d):
    n = len(str_1)
    m = len(str_2)
    a = 0 #uzun stringte kaliplara ayirmak icin
    c = 0 #kisa string dolasmak icin
    kacTane = 0
    f = m

    while(a<=n-f):
        b = 0 #hatayı kontrol etmek icin
        for i in range(a,m):
            if(b>d):
                break
            if(str_1[i]==str_2[c]):
                c += 1
            else:
                c += 1
                b += 1

        if(b<=d):
            for i in range(a,m):
                print(str_1[i])
            kacTane += 1
        if(m<n):
            m += 1
        a += 1
        c = 0
    if(kacTane>0):
        return (True,kacTane)
    else:
        return (False,kacTane)

a = input("Bir string giriniz: ")
b = input("Aranacak olani giriniz: ")
error = int(input("Hata oranini giriniz: "))
print(search_with_error(a,b,error))
