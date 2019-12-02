def create_mat(nrows, ncols):
    mat = []
    for i in range(nrows):
        mat.append([])
        for j in range(ncols):
            mat[i].append(0)
    return mat

create_mat(2,3)

def dotplot(seq1, seq2):
    mat = create_mat( len (seq1), len (seq2))
    for i in range( len (seq1)):
        for j in range( len (seq2)):
            if seq1[i] == seq2[j]:
                mat[i][j] = 1
    return mat

dotplot("ATGA","AGTA")

def print_dotplot(mat, s1, s2):
    import sys
    sys.stdout.write(" " + s2+"\n")
    for i in range( len (mat)):
        sys.stdout.write(s1[i])  #printten farklı olarak sadece karakter dizisini alır
        for j in range( len (mat[i])):
            if mat[i][j] >= 1:
                sys.stdout.write("∗")
            else :
                sys.stdout.write(" ")
    sys.stdout.write("\n")

def test():
    s1 = "CGATATAG"
    s2 = "TATATATT"
    mat1 = dotplot(s1, s2)
    print_dotplot(mat1, s1, s2)

test()

def extended_dotplot (seq1, seq2, window, stringency):
    mat = create_mat( len (seq1), len (seq2))  #iki boyutlu dizi olusturdu
    start = int (window/2) 
    for i in range(start, len (seq1)-start):
        for j in range(start, len (seq2)-start):
            matches = 0
            l=j - start
            for k in range(i-start, i+start+1):
                print(seq1[k],seq2[l])
                if seq1[k] == seq2[l]: 
                    matches += 1
                l += 1
                if matches >= stringency: 
                    mat[i][j] = 1
    return mat

def test():
    s1 = "CGATATAGATT"
    s2 = "TATATAGTAT"
    mat2 = extended_dotplot(s1, s2, 5, 4)
    print(mat2)
    print_dotplot(mat2, s1, s2)

test()
