score = 0
with open("Data.txt") as file:
  lines = file.readlines()

for line in lines:
  input = line.split()
  # Player 1: Rock
  if input[0] == 'A':
    if input[1] == 'X': # Lose => Scissor
      score += (0+3)
    if input[1] == 'Y': # Draw => Rock
      score += (3+1)
    if input[1] == 'Z': # Win => Paper
      score += (6+2) 
  #Player 1: Paper (Symbol + Win/Loss/Draw)
  if input[0] == 'B': # Paper
    if input[1] == 'X': # Lose => Rock
      score += (0+1)
    if input[1] == 'Y': # Draw => Paper
      score += (3+2)
    if input[1] == 'Z': # Win => Scissors
      score += (6+3) 
  # Player 1: Scissors
  if input[0] == 'C':
    if input[1] == 'X': # Lose < Paper
      score += (0+2)
    if input[1] == 'Y': # Draw > Scissors
      score += (3+3)
    if input[1] == 'Z': # Win > Rock
      score += (6+1) 
  print(input[0] + " " + input[1])
print(score)