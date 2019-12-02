def OverlapGraph(seq):
    k = len(seq[0])
    set={}
    for i in range(len(seq)):
        n=0
        for j in range(len(seq)):
            if seq[i][1:]==seq[j][:k-1] and i!=j:
                if n==1:
                    set[seq[i]].append(seq[j])
                else:
                    set[seq[i]]=[seq[j]]
                    n=1
    return set

t=["ATG", "AGG" ,"TGC", "TCC", "GTC", "GGT", "GCA", "CAG"]
OverlapGraph(t)

def DeBruijn(Text,k):
    path={}
    for i in range(len(Text)-k+1):
        k_mer=Text[i:i+k]
        for j in path.keys():
            if k_mer[:k-1]==j:
                path[k_mer[:k-1]].append(k_mer[1:])
                break
        else:
            path[k_mer[:k-1]]=[k_mer[1:]]
    return path

DeBruijn("ATGCAGGTCC",4)
