text = input().strip()
k = int(input().strip())

counts = {}

for i in range(len(text) - k + 1):
    pattern = text[i:i+k]
    counts[pattern] = counts.get(pattern, 0) + 1

max_count = max(counts.values())

result = [pattern for pattern, count in counts.items() if count == max_count]

print(*result)
