score = 0
with open("Data.txt") as file:
  lines = file.readlines()

for line in lines:
  input = line.split()
  # Player 1: Rock
  if input[0] == 'A':
    if input[1] == 'X': # Rock = Rock
      score += (1+3)
    if input[1] == 'Y': # Rock < Paper
      score += (2+6)
    if input[1] == 'Z': 
      score += (3+0) # Rock > Scissors
  #Player 1: Paper (Symbol + Win/Loss/Draw)
  if input[0] == 'B':
    if input[1] == 'X': # Paper > Rock
      score += (1+0)
    if input[1] == 'Y': # Paper = Paper
      score += (2+3)
    if input[1] == 'Z':
      score += (3+6) # Paper < Scissors
  # Player 1: Scissors
  if input[0] == 'C':
    if input[1] == 'X': # Scissors < Rock
      score += (1+6)
    if input[1] == 'Y': # Scissors > Paper
      score += (2+0)
    if input[1] == 'Z':
      score += (3+3) # Scissors = Scissors
  print(input[0] + " " + input[1])
print(score)