from itertools import product

def hamming_distance(s1, s2):
    return sum(a != b for a, b in zip(s1, s2))

def count_with_mismatches(text, pattern, d):
    k = len(pattern)
    count = 0
    for i in range(len(text) - k + 1):
        if hamming_distance(text[i:i+k], pattern) <= d:
            count += 1
    return count

def frequent_words_with_mismatches(text, k, d):
    nucleotides = "ACGT"
    patterns = [''.join(p) for p in product(nucleotides, repeat=k)]

    max_count = 0
    frequent_patterns = []

    for pattern in patterns:
        count = count_with_mismatches(text, pattern, d)

        if count > max_count:
            max_count = count
            frequent_patterns = [pattern]
        elif count == max_count:
            frequent_patterns.append(pattern)

    return frequent_patterns

text = input("Enter the string: ").strip()
k = int(input("Enter k: "))
d = int(input("Enter d: "))

result = frequent_words_with_mismatches(text, k, d)
print(*result)
