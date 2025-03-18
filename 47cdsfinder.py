import sys
import mcb185
import sequence

file = sys.argv[1]
length_of_aas = int(sys.argv[2])


def cds_finder(dna, length_of_aas):
	
	tranlsated_proteins = []
    
	aas = mcb185.translate(seq)
    
	orfs = aas.split('*')
    
	for orf in orfs:
		if 'M' in orf:
			start = orf.find('M')
			protein = orf[start:]
    		
			final_protein = protein + '*'
			
			if len(final_protein) >= length_of_aas:
				tranlsated_proteins.append(final_protein)
    		
	return tranlsated_proteins 
    	
for defline, seq in mcb185.read_fasta(file):
	words = defline.split()
	identifier = words[0]
	seq_num = 0
	reverse_strand = mcb185.anti_seq(seq)	
	
	for frame in range(3):
		for forward in cds_finder(seq[frame:], length_of_aas):
			seq_num += 1
			print('>', identifier, "-proto", seq_num, sep='')
			print(forward)
	for reverse in cds_finder(reverse_strand[frame:], length_of_aas):
		seq_num += 1
		print('>', identifier, "-proto", seq_num, sep='')
		print(reverse)
   
           