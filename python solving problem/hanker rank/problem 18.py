# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

s = input()
k = input()

matches = list(re.finditer(r'(?=' + re.escape(k) + r')', s))

if matches:
    for m in matches:
        start = m.start()
        end = start + len(k) - 1
        print((start, end))
else:
    print((-1, -1))
