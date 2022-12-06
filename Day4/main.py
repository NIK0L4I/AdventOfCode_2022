duplicates = 0
overlaps = 0
#(One set is contained in the other)
def containsArray(arr1, arr2):
  if int(arr1[0]) <= int(arr2[0]) and int(arr1[1]) >= int(arr2[1]):
    return True
  if int(arr1[0]) >= int(arr2[0]) and int(arr1[1]) <= int(arr2[1]):
    return True
  return False

# One set overlaps with the other
def overlapArray(arr1, arr2):
  if containsArray(arr1, arr2):
    return True
  if int(arr1[1]) < int(arr2[0]):
    return False
  if int(arr1[0]) > int(arr2[1]):
    return False
  return True
  
with open("Data.txt") as f:
  lines = f.readlines()

#Part 1 (One set is contained in the other)
for line in lines:
  input = line.split(",")
  firstElv = input[0]
  secondElv = input[1]
  firstSection = firstElv.split("-")
  secondSection = secondElv.split("-")
  #print(firstSection, secondSection, containsArray(firstSection, secondSection))
  print(firstSection, secondSection, overlapArray(firstSection, secondSection))
  if containsArray(firstSection, secondSection):
    duplicates += 1
  # Part 2
  if overlapArray(firstSection, secondSection):
    overlaps += 1
    
print(duplicates)
print(overlaps)


