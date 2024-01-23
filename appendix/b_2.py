from itertools import combinations

l, c = map(int, input().split())
alphabets = list(input().split())
vowels = {"a", "e", "i", "o", "u"}


candidates = list(combinations(alphabets, l))
sorted_candidates = []
for cand in candidates:
    sorted_candidates.append("".join(sorted(cand)))


result = set()

for cand in sorted_candidates:
    vowels_count = 0
    consonants_count = 0
    for c in cand:
        if c in vowels:
            vowels_count += 1
        else:
            consonants_count += 1
    
    if vowels_count >= 1 and consonants_count >= 2:
        result.add(cand)

for word in sorted(result):
    print(word)



