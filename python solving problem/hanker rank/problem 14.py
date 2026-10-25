# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

# All possible combinations of k indices
all_combinations = list(combinations(range(n), k))

# Count combinations containing at least one 'a'
count = 0

for indices in all_combinations:
    for i in indices:
        if letters[i] == 'a':
            count += 1
            break

probability = count / len(all_combinations)

print(round(probability, 4))
s