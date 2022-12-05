max = 0
#Part Two
second = 0
third = 0

current = 0

with open("Data.txt") as f:
  lines = f.readlines()

for line in lines:
  if line.strip() != "":
    current += int(line)
  else:
    if current > max:
      third = second
      second = max
      max = current
    elif current > second:
      third = second
      second = current
    elif current > third:
      third = current
    current = 0
print(max+second+third)