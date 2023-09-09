# Frequent Words with Mismatches and Reverse Complements Problem
# Find the most frequent k-mers (with mismatches and reverse complements) in a DNA string.
# Given: A DNA string Text as well as integers k and d.
# Return: All k-mers Pattern maximizing the sum Countd(Text, Pattern) + Countd(Text, Pattern) over all possible k-mers.

# Sample Dataset:
# ACGTTGCATGTCGCATGATGCATGAGAGCT
# 4 1
# Sample Output
# ATGT ACAT

genome = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
d = 1

def hammingd(a,b):
    count = 0
    for i in range(len(a)):
        if a[i]!= b[i]:
            count = count + 1
    return count

chars = "ACGT"
def neighbors(pattern, d):
    assert(d <= len(pattern))

    if d == 0:
        return [pattern]

    r2 = neighbors(pattern[1:], d-1)
    r = [c + r3 for r3 in r2 for c in chars if c != pattern[0]]

    if (d < len(pattern)):
        r2 = neighbors(pattern[1:], d)
        r += [pattern[0] + r3 for r3 in r2]

    return r

def revcomp(pattxrn):
    revpattxrn = pattxrn[::-1]

    counterpattxrn = revpattxrn.replace('A','P').replace('G','Q')
    counterpattxrn = counterpattxrn.replace('T','A').replace('C','G')
    counterpattxrn = counterpattxrn.replace('P','T').replace('Q','C')
    
    return counterpattxrn

allkmers = []
allkmersrevcom = []

for i in range(len(genome)-k+1):
    temp = neighbors(genome[i:i+k],d)
    for x in range(len(temp)):
        allkmers.append(temp[x])
        
for i in range(len(genome)-k+1):
     allkmers.append(genome[i:i+k])

freq1 = [0]*len(allkmers)
        
for i in range(len(allkmers)):
    for j in range(len(genome)-k+1):
        if hammingd(allkmers[i],genome[j:j+k]) <= d:
            freq1[i] = freq1[i] + 1
        
for i in range(len(allkmers)):
    allkmersrevcom.append(revcomp(allkmers[i]))

freq2 = [0]*len(allkmersrevcom)
        
for i in range(len(allkmersrevcom)):
    for j in range(len(genome)-k+1):
        if hammingd(allkmersrevcom[i],genome[j:j+k]) <= d:
            freq2[i] = freq2[i] + 1

freq = [0]*len(freq1)
for i in range(len(freq1)):
    freq[i] = freq1[i] + freq[i]

freqpattern = []
            
for i in range(len(freq)):
    if freq[i] == max(freq):
        freqpattern.append(allkmers[i])
        
freqpattern = list(dict.fromkeys(freqpattern))

for i in range(len(freqpattern)):
    print(freqpattern[i])
