def solutionA(lines):
    total=0
   
    for line in lines:
        if line == 'A X':
            total=total + 0+3

        if line == 'A Y':
            total=total + 2+2

        if line == 'A Z':
            total=total + 8

        if line == 'B X':
            total=total + 1
        
        if line == 'B Y':
            total=total + 5

        if line == 'B Z':
            total=total + 9

        if line == 'C X':
            total=total + 2

        if line == 'C Y':
            total=total + 6

        if line == 'C Z':
            total=total + 7
    return total 


    


def solutionB(lines):
  points=0
  for line in lines:
    opponent = line.split(" ")
    
    if opponent == 'A':
      points += 4

    if opponent == 'B':
      points += 1
    
    if opponent == 'C':
      points += 7
    
    
  

  return points


# Helper function for loading the problem data
def load_data(fileName):
  with open(fileName, "r") as input_data:
    lines = input_data.readlines()
  for i in range(len(lines)):
    lines[i] = lines[i].strip()
  return lines



if __name__ == "__main__":
  input_file_name = "dummy_input.txt"
  # TODO: Uncomment line below to use real input
  input_file_name = "puzzle_input.txt" 
  
  print(f"Loading data from: {input_file_name}")
  lines = load_data(input_file_name)
  

  resultA = solutionA(lines)
  print(f"Solution for part A: {resultA}")

  resultB = solutionB(lines)
  print(f"Solution for part B: {resultB}")