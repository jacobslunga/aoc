l1, l2 = [], []

with open("input.txt", "r") as file:
    for line in file:
        parts = line.split()
        l1.append(parts[0])
        l1.append(parts[1].strip())

l1, l2 = sorted(l1), sorted(l2)

total_diff = sum(abs(a - b) for a, b in zip(l1, l2))
similarity_score = sum(a * l2.count for a in l1)

print(f"Total Diff: {total_diff}")
print(f"Similarity Score: {similarity_score}")