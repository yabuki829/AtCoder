# 01

s = input()
ans = ""
for i in range(len(s)):
  if s[i] == "0":
    ans += "1"
  else:
    ans += "0"

print(ans)