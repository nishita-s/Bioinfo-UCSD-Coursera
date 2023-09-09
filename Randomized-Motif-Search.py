import random
import numpy as np
from pprint import pprint

def get_kmers(text, k):
    kmers = []
    for i in range(len(text)-k+1):
        kmers.append(text[i:i+k])
    return kmers
    
def get_suffix(text):
    return text[1:]

def get_prefix(text):
    return text[:len(text)-1]

def get_profile(motifs):
    """gets the profile matrix for a given set of motifs, adds 1 to each element in the matrix (pseudocounts) and returns that
    profile: list of dictionaries"""
    
    motifs = list(zip(*motifs))
    profile = []
    
    for m in motifs:
        nt,counts = np.unique(m, return_counts=True)
        counts = counts/sum(counts)
        profile.append(dict(zip(nt,counts)))

    for p in profile:
        for nt in 'ACGT':
            if nt not in p.keys():
                p.update({nt: 0})
    
    #Pseudocounts
    for p in profile:
        for k in p:
            p.update({k: p[k]+1})
    
    return profile

def get_kmer_probab(kmer, profile):
    """gets the probability of a kmer acc to a profile"""
    probab = 1
    for i, nt in enumerate(kmer):
        probab *= profile[i][nt]

    return probab


def get_motifs(profile, DNA, k):
    """args:
    profile: list of dictionary
    DNA: strings separated by spaces
    k: size of kmer
    returns motifs from DNA acc to given profile"""
    
    sDNA = DNA.split()
    motifs = []
    for dna in sDNA:
        maxprobab, index = 0,0
        for i in range(len(dna)-k+1):
            probab = 1
            for j,nt in enumerate(dna[i:i+k]):
                probab *= profile[j][nt]

            if probab > maxprobab:
                maxprobab = probab
                index = i
            
        motifs.append(dna[index:index+k])
    
    return motifs

def get_score(motifs):
    t = len(motifs)
    motifs = list(zip(*motifs))
    
    score = 0
    for m in motifs:
        _,counts = np.unique(m, return_counts=True)
        score += t-max(counts)
    return score
def get_random_motifs(sDNA, k):
    """sDNA: list of sequences of a dna
    k: size of kmer
    returns randomly generated set of motifs (one kmer from each sequence)"""

    motifs = []
    for s in sDNA:
        i = np.random.randint(0, len(s)-k)
        motifs.append(s[i:i+k])
    
    return motifs

def RandomizedMotifSearch(DNA, k):
    sDNA = DNA.split()
    motifs = get_random_motifs(sDNA, k)
    best_motifs = motifs[:]
    best_score = get_score(best_motifs)

    while True:
        profile = get_profile(motifs)
        motifs = get_motifs(profile, DNA, k)
        motif_score = get_score(motifs)
        if motif_score < best_score:
            best_motifs = motifs[:]
            best_score = motif_score
        else:
            return best_motifs
