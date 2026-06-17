pattern = input().strip()
genome = input().strip()

positions = []
k = len(pattern)

for i in range(len(genome) - k + 1):
    if genome[i:i+k] == pattern:
        positions.append(str(i))

print(" ".join(positions))
