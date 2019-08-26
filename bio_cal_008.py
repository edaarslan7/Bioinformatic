pdict = {'AA':0, 'AC':1, 'AG':2,'AT':3,'CA':4,'CC':5,'CG':6,'CT':7,'GA':8,'GC':9,'GG':10,'GT':11,'TA':12,'TC':13,'TG':14,'TT':15}

def symboltonumber(symbol): 
    if(symbol=='A'):
        return 0
    elif(symbol=='C'):
        return 1
    elif(symbol=='G'):
        return 2
    else:
        return 3
        
def PREFIX(pattern):
    return pattern[0:len(pattern)-1]
    
def LASTSYMBOL(pattern):
    return pattern[len(pattern)-1]
    
def patterntonumber(pattern):
    if(len(pattern)==0):
        return 0
    else:
        symbol = LASTSYMBOL(pattern)
        prefix = PREFIX(pattern)
        return 4*patterntonumber(prefix) + symboltonumber(symbol)
        
def computing_frequencies(text,k):
    frequency_array = [0] * (4**k)
    for i in range((4**k)-1):
        frequency_array[i] = 0
    for i in range(len(text)-1):
        pattern = text[i:k]
        print(pattern)
        j = patterntonumber(pattern)
        frequency_array[j] += 1
        k += 1
    return frequency_array
    
def numbertosymbol(index):
    if(index==0):
        return 'A'
    elif(index==1):
        return 'C'
    elif(index==2):
        return 'G'
    else:
        return 'T'
        
def quotient(index,a):
    a = 4
    return index//a
    
def remainder(index,a):
    a = 4
    return index%a
    
def numbertopattern(index,k):
    if(k==1):
        return numbertosymbol(index)
    prefixindex = quotient(index,4)
    r = remainder(index,4)
    symbol = numbertosymbol(r)
    prefixpattern = numbertopattern(prefixindex,k-1)
    return (prefixpattern + symbol)
    
def faster_frequent_words(text,k):
    frequent_patterns = []
    frequency_array = computing_frequencies(text,k)
    maxCount =frequency_array[0]
    for i in range(1,4**k-1):
        if(frequency_array[i]>maxCount):
            maxCount = frequency_array[i]
    for i in range(4**k):
        if(frequency_array[i]==maxCount):
            pattern = numbertopattern(i,k)
            frequent_patterns.append(pattern)
    return frequent_patterns
    
def finding_frequent_words_by_sorting(text,k):
    frequent_patterns = []
    index = []
    count = [1]*(len(text)-1)
    a = k
    for i in range(len(text)-k+1):
        pattern = text[i:a]
        index.append(patterntonumber(pattern))
        a += 1
    sorted_index = sorted(index) 
    for j in range(1,len(text)-k+1):
        
        if(sorted_index[j]==sorted_index[j-1]):
            count[j] = count[j-1] + 1
    max_count = max(count)
    for i in range(len(text)-k):
        if(count[i]==max_count):
            pattern = numbertopattern(sorted_index[i],k)
            frequent_patterns.append(pattern)
    return frequent_patterns,count,sorted_index
    
def clump_finding(genome,k,t,l):
    frequent_patterns =[]
    frequency_array =[]
    clump = [0]*(4**k-1)
    for i in range(len(genome)-l):
        text = genome[i:l]
        frequency_array = computing_frequencies(text,k)
        for j in range(4**k-1):
            if(frequency_array[j]>=t):
                clump[j] = 1
    for i in range(4**k-1):
        if(clump[i]==1):
            pattern = numbertopattern(i,k)
            frequent_patterns.append(pattern)
    return frequent_patterns
    
def better_clump_finding(genome,k,t,l):
    frequent_patterns = []
    clump = [0]*(4**k-1)
    text = genome[0:l]
    frequency_array = computing_frequencies(text,k)
    for i in range(4**k-1):
        if(frequency_array[i]>=t):
            clump[i]=1
    for i in range(1,len(genome)-l):
        first_pattern  = genome[i-1:k]
        index =  patterntonumber(first_pattern)
        frequency_array[index] = frequency_array[index] -1
        last_pattern = genome[i+l-k:k]
        index = patterntonumber(last_pattern)
        frequency_array[index] = frequency_array[index] +1
        if(frequency_array[index]>=t):
            clump[index] = 1
    for i in range(4**k-1):
        if(clump[i] == 1):
            pattern = numbertopattern(i,k)
            frequent_patterns.append(pattern)
    return frequent_patterns

def SUFFIX(pattern):
    return pattern[1:]
    
def first_symbol(pattern):
    return pattern[0]
    
#hamming distance problem  ayni uzunluktaki iki dna parcasini kiyaslayip farklarini hesapliyor
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
        
def approximate_pattern_count(text,pattern,d): #texti patternin uzunlugu kadar parcalayip patternle kiyasliyor d hata payi  ile 
    count = 0
    a = len(pattern)
    for i in range(len(text)-a+1):
        pattern_1 = text[i:a]
        if(hamming_distance(pattern,pattern_1)<=d):
            count += 1
        a += 1
    return count
    
def neighbors(pattern,d):  #patterni d hata payi ele alinarak ortaya cikabilecek tüm mutasyon olasiliklari hesapliyor
    nucleotide = {'A','C','T','G'}
    if(d==0):
        return pattern
    if(len(pattern)==1):
        return nucleotide
    neighborhood = []
    suffix_neighbors = neighbors(SUFFIX(pattern),d)
    
    for text in suffix_neighbors:
       # print(suffix_neighbors)
        if(hamming_distance(SUFFIX(pattern),text)<d):
            for x in nucleotide:
                neighborhood.append(x+text)
        else:
            neighborhood.append(first_symbol(pattern)+text)
    return neighborhood
#recursive oldugu icin cok buyuk patternlerde hata aliyoruz

def frequent_words_with_mismatches(text,k,d): #d hata payi ile textteki patternlerin frekanslarini hesapliyor
    frequent_patterns = []
    close = [0]*(4**k-1)
    frequency_array = [0]*(4**k-1)
    a = k-1
    for i in range(len(text)-k+1):
        neighborhood = neighbors(text[i:a],d)
        for pattern in neighborhood:
            index = patterntonumber(pattern)
            close[index] = 1
        a += 1
    for i in range(4**k-1):
        if(close[i]==1):
            pattern = numbertopattern(i,k)
            frequency_array[i] = approximate_pattern_count(text,pattern,d)
    maxCount = max(frequency_array)
    for i in range(4**k-1):
        if(frequency_array[i]==maxCount):
            pattern = numbertopattern(i,k)
            frequent_patterns.append(pattern)
    return frequent_patterns
    
def finding_frequent_words_with_mismatches_by_sorting(text,k,d):
    frequent_patterns = []
    neighborhoods = []
    a = k
    for i in range(len(text)-k+1):
        neighborhoods.extend(neighbors(text[i:a],d))  #extend ile iki listeyi birlestirerek ekliyor 
                                #append ile ekleme yaptiginda neighbors fonksiyonundan gelen listeyi tek eleman olarak ekliyor :)
        a += 1
    neighborhood_array = neighborhoods
    index = [0]*(len(neighborhoods)-1)
    count = [0]*(len(neighborhoods)-1)
    for i in range(len(neighborhoods)-1):
        pattern = neighborhood_array[i]
        index[i] = patterntonumber(pattern)
        count[i] = 1
    sorted_index = sorted(index)
    for i in range(len(neighborhoods)-2):
        if(sorted_index[i] == sorted_index[i+1]):
            count[i+1] = count[i]+1
    max_count = max(count)
    for i in range(len(neighborhoods)-1):
            if(count[i] == max_count):
                pattern = numbertopattern(sorted_index[i],k)
                frequent_patterns.append(pattern)
    return frequent_patterns    
