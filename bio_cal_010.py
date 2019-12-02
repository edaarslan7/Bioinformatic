def Skew(Genome):
    set={'C':-1,'G':1,'A':0,'T':0}
    skew=[0]
    for i in range(len(Genome)):
        skew.append(skew[i]+set[Genome[i]])
    return skew

def MinimumSkew(Genome):
    skew=Skew(Genome)
    Mins=[]
    mins=min(skew)
    for i in range(len(skew)):
        if skew[i]==mins:
            Mins.append(i)
    return Mins


MinimumSkew("ATCGAATGA")
