duplicates = 0
def containsArray(arr1, arr2):
  if int(arr1[0]) <= int(arr2[0]) and int(arr1[1]) >= int(arr2[1]):
    return True
  if int(arr1[0]) >= int(arr2[0]) and int(arr1[1]) <= int(arr2[1]):
    return True
  return False

with open("Data.txt") as f:
  lines = f.readlines()

for line in lines:
  input = line.split(",")
  firstElv = input[0]
  secondElv = input[1]
  firstSection = firstElv.split("-")
  secondSection = secondElv.split("-")
  print(firstSection, secondSection, containsArray(firstSection, secondSection))
  if containsArray(firstSection, secondSection):
    duplicates += 1
  
print(duplicates)


