#gc_content_calculator.py
#Code_to_cal_gc_content_manually
#define_seq
dna_seq="ATGCATGCATGCATCGATCGATCGGCGCGCGCGCT"
#count_g's_c'c
g_count = dna_seq.count('G')
c_count = dna_seq.count('C')
total_length = len(dna_seq)
gc_per = (g_count +c_count)/total_length * 100
print(f"DNA seq: {dna_seq})
print(f"Total length: {total_length})
print(f"GC_Content: {gc_per:.2f}%)
