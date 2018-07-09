
def to_rna(dna_strand):
    dict={'G':'C','C':'G','T':'A','A':'U'}
    for i in dna_strand:
        if i in dict:
            continue
        else:
            raise ValueError("enter valid dna")
    return ''.join(dict[x] for x in dna_strand )
