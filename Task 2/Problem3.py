pattern = input().strip()

complement = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

reverse_complement = ''.join(complement[n] for n in reversed(pattern))

print(reverse_complement)
