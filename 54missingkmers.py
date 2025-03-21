import sys
import mcb185
import itertools

file = (sys.argv[1])
kcount = {}   # atg: 1 ctc: 2
missing_kmers = []
n = 0

for k in range(1, 10): # start k at 1 and increase until missing kmers
    for defline, seq in mcb185.read_fasta(file):
        rev_seq = mcb185.anti_seq(seq) # need to search both strands 
        strands = {'f_strand': seq, 'r_strand': rev_seq} #dictionary 

        for strand_type, strand in strands.items():  # for both f and r strand
            for i in range(len(strand)- k + 1): 
                kmer = strand[i:i+k]
                if kmer not in kcount:
                    kcount[kmer] = 0 # checks if kmer in dictinary if not it initializes it
                kcount[kmer] +=1   #send to k count

    for nts in itertools.product('ACGT', repeat=k): # generates all possible kmers
        kmer = ''.join(nts)
        if kmer not in kcount: 
            n += 1
            missing_kmers.append(kmer) #append missing kmers not in count to container

    if n > 0:  #
        for kmer in missing_kmers:
            print(kmer) #missing kmer printed 
        print(n, k)
        break