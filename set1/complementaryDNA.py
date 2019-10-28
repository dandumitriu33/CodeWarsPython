def DNA_strand(dna):
    resulting_strand = ''
    complements = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    for i in dna:
        resulting_strand = resulting_strand + complements[i.upper()]
    resulting_strand.upper()
    return resulting_strand


print(DNA_strand('tata'))
