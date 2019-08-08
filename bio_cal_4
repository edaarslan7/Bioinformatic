def reverse_complement(str1):
   # print("eski değer : ",str1)
    for i in range(len(str1)):
        if(str1[i]=='a'):
            str1 = str1[0:i] + 't' + str1[i+1:len(str1)]
        elif(str1[i]=="t"):
             str1 = str1[0:i] + 'a' + str1[i+1:len(str1)]
        elif(str1[i]=="g"):
             str1 = str1[0:i] + 'c' + str1[i+1:len(str1)]
        else:
             str1 = str1[0:i] + 'g' + str1[i+1:len(str1)]
    return str1[::-1]

def search_norm_comp(str1,s):
    g = reverse_complement(s)
    liste = []
    a,sayac = 0,0
    k = len(s)
    while(k<=len(str1)):
            for i in range(a,k):
                str2=str1[a:k]
            a+=1
            k+=1
            liste.append(str2)
    for i in range(len(liste)):
          if(s==liste[i] or g==liste[i]):
              sayac+=1
    return(sayac)

str1 = input("metni giriniz: ")
s = input("aranacak metni giriniz: ")
search_norm_comp(str1,s)
