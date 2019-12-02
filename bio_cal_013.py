def Count(Motifs):
    count=[]
    if len(Motifs) != 1:
        for i in range(len(Motifs[0])):
            A = 0;C = 0;G = 0; T = 0
            for j in range(len(Motifs)):
                if Motifs[j][i] == 'A': A += 1
                if Motifs[j][i] == 'C': C += 1
                if Motifs[j][i] == 'G': G += 1
                if Motifs[j][i] == 'T': T += 1
            count.append([A, C, G, T])
        count=[list(x) for x in zip(*count)]
    else:
        for j in range(len(Motifs[0])):
            A = 0;C = 0;G = 0; T = 0
            if Motifs[0][j] == 'A': A += 1
            if Motifs[0][j] == 'C': C += 1
            if Motifs[0][j] == 'G': G += 1
            if Motifs[0][j] == 'T': T += 1
            count.append([A, C, G, T])
        count = [list(x) for x in zip(*count)]
    return count


Count(dna)


def Profile(Motifs):
    count=Count(Motifs)
    profile=count
    for i in range(4):
        for j in range(len(Motifs[0])):
            profile[i][j]=count[i][j]/len(Motifs)
    return profile

Profile(dna)

def Consensus(Motifs):
    set = {0:'A', 1:'C', 2:'G', 3:'T'}
    consensus=''
    if len(Motifs[0])!=1:
        for i in range(len(Motifs[0])):
            A = 0; C = 0; G = 0; T = 0
            for j in range(len(Motifs)):
                if Motifs[j][i]=='A': A+=1
                if Motifs[j][i]=='C': C+=1
                if Motifs[j][i]=='G': G+=1
                if Motifs[j][i]=='T': T+=1
            S=[A,C,G,T]
            Max=max(S)
            for n in range(4):
                if S[n]==Max:
                    consensus=consensus+set[n]
                    break
    else: print('Motifs has one string')
    return consensus


Consensus(dna)

def Score(Motifs):
    consensus=Consensus(Motifs)
    score=0
    for i in range(len(Motifs)):
        score+=hamming_distance(consensus,Motifs[i])
    return score


Score(dna)
