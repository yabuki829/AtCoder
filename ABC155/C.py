N = int(input())

d = {}

for _ in range(N):
  S = input()

  if S in d:
    d[S] += 1
  else:
    d[S] = 1
max = max(d.values())

for s in sorted(k for k in d if d[k] == max):
  print(s)

