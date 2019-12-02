def validate_dna (dna):
    Dna_1 = dna.upper()
    valid = Dna_1.count("A") + Dna_1.count("C") + Dna_1.count("G") + Dna_1.count("T")
    if valid == len (Dna_1): 
        return True
    else: 
        return False

def translate_codon(str_1):

    trans_cod = { "GCT":"A", "GCC":"A", "GCA":"A", 
                  "GCG":"A", "TGT":"C", "TGC":"C",
                  "GAT":"D", "GAC":"D", "GAA":"E", 
                  "GAG":"E", "TTT":"F", "TTC":"F",
                  "GGT":"G", "GGC":"G", "GGA":"G", 
                  "GGG":"G", "CAT":"H", "CAC":"H",
                  "ATA":"I", "ATT":"I", "ATC":"I",
                  "AAA":"K", "AAG":"K", "TTA":"L", 
                  "TTG":"L", "CTT":"L", "CTC":"L", 
                  "CTA":"L", "CTG":"L", "ATG":"M", 
                  "AAT":"N", "AAC":"N", "CCT":"P", 
                  "CCC":"P", "CCA":"P", "CCG":"P",
                  "CAA":"Q", "CAG":"Q", "CGT":"R", 
                  "CGC":"R", "CGA":"R", "CGG":"R", 
                  "AGA":"R", "AGG":"R", "TCT":"S", 
                  "TCC":"S", "TCA":"S", "TCG":"S", 
                  "AGT":"S", "AGC":"S", "ACT":"T", 
                  "ACC":"T", "ACA":"T", "ACG":"T",
                  "GTT":"V", "GTC":"V", "GTA":"V", 
                  "GTG":"V", "TGG":"W","TAT":"Y", 
                  "TAC":"Y", "TAA":"_", "TAG":"_", "TGA":"_"}
    if str_1 in trans_cod: 
        return trans_cod[str_1]
    else : 
        return None

translate_codon("CCA")

def Translate_Dna (dna, ini_pos = 0):  
    assert validate_dna(dna)  #assert if else durumuna eşittir.
    Dna_1 = dna.upper()
    seq_aa = " "
    print(Dna_1)
    a = (len(Dna_1))
    for pos in range(ini_pos, a-2 ,3):
        cod = Dna_1[pos:pos+3]
        seq_aa += translate_codon(cod)
    return seq_aa


Translate_Dna("ATTTAGCGTA",1)


def codon_usage(dna_seq, b = 'K'): #verilen aa nın dna diziliminde bulunup bulunmadıgı ve dagılımı
    assert validate_dna(dna_seq)  
    seqm = dna_seq.upper()
    dic = {}
    total = 0
    a=(len(seqm))
    print(dna_seq,a)
    for i in range (0, a-2, 3):
        cod = seqm[i:i+3]
        if translate_codon(cod) == b:
            if cod in dic:
                dic[cod] += 1
            else : 
                dic[cod] = 1
            total += 1
            #print(total,dic)
        if total >0:
            for k in dic:
                print(cod,k,dic,dic[k],total)
                dic[k] /= total
    return dic

codon_usage("aaaattgttaaagccaaaa",'K')

def reverse_complement (dna):
    assert validate_dna(dna)
    comp = ""
    for c in dna.upper():
        if c == 'A':
            comp = "T" + comp
        elif c == "T":
            comp = "A" + comp
        elif c == "G":
            comp = "C" + comp
        elif c== "C":
            comp = "G" + comp
    return comp

def reading_frames (dna_seq):
    assert validate_dna(dna_seq)
    res = []
    res.append(Translate_Dna(dna_seq ,0))
    res.append(Translate_Dna(dna_seq ,1))
    res.append(Translate_Dna(dna_seq ,2))
    rc = reverse_complement(dna_seq)
    res.append(Translate_Dna(rc,0))
    res.append(Translate_Dna(rc,1))
    res.append(Translate_Dna(rc,2))
    return res

reading_frames("AGCGATATAG")

def protein (amino):
    amino = amino.upper()
    current_prot = []
    proteins = []
    for aa in amino:
        print(aa)
        if aa == "_": #_ = STOP
            if current_prot:
                print(current_prot)
                for p in current_prot:
                    print(p)
                    proteins.append(p)
                current_prot = []
        else :
            if aa == "M":
                current_prot.append("")
            for i in range( len (current_prot)):
                current_prot[i] += aa
    return proteins

protein("fmmmfl_s_t")


def insert_prot_ord (prot, list_prots):
    i=0
    while i < len (list_prots) and len (prot) < len (list_prots[i]):
        i += 1
    list_prots.insert(i, prot)


def all_orfs_ord (dna_seq, minsize = 0):

    assert validate_dna(dna_seq)
    rfs = reading_frames (dna_seq)
    res = []
    for rf in rfs:
        prots = protein(rf)
        for p in prots:
            if (len(p) > minsize): 
                insert_prot_ord(p, res)
    return res

all_orfs_ord("ATGTGTCATTAATACATT",0)
