#Reverse Complement
def reverse_complement(str1):
    print("eski değer : ",str1)
    for i in range(len(str1)):
        if(str1[i]=='a'):
            str1 = str1[0:i] + 't' + str1[i+1:len(str1)]
        elif(str1[i]=="t"):
             str1 = str1[0:i] + 'a' + str1[i+1:len(str1)]
        elif(str1[i]=="g"):
             str1 = str1[0:i] + 'c' + str1[i+1:len(str1)]
        else:
             str1 = str1[0:i] + 'g' + str1[i+1:len(str1)]
    print("son değer : ",str1[::-1]) 

str1 = input("Bir string giriniz: ")
print(reverse_complement(str1))
