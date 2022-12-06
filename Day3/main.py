sum = 0
sumBadges = 0
with open("Data.txt") as f:
  lines = f.readlines()

# Part 1
for line in lines:
  firstPart = line[len(line)//2:]
  secondPart = line[:len(line)//2]
  for c in firstPart:
    if c in secondPart:
      if c.islower():
        sum += ord(c)-96
        break
      if c.isupper():
        sum += ord(c)-96+26+32
        break

# Part 2
for i in range(0,(len(lines)),3):
  for c in lines[i]:
    if c in lines[i+1] and c in lines[i+2]:
      if c.islower():
        sumBadges += ord(c)-96
        break
      elif c.isupper():
        sumBadges += ord(c)-96+26+32
        break
print(sum)
print(sumBadges)
  