def hamming_distance(s1,s2):
    if(len(s1)==len(s2)):
        p = 0
        diff = 0
        for i in s1:
            if(i!=s2[p]):
                diff += 1
                p += 1
            else:
                p += 1
        return diff
    else:
        print("Esit uzunlukta olmali...")
        
     
str1 = input("Bir DNA parcasi giriniz: ")
str2 = input("Baska bir tane daha giriniz: ")
hamming_distance(str1,str2)
