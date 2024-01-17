
from pathlib import Path

dir_path = Path(__file__, '..').resolve()
file_name = "puzzle_input.txt"
full_path = dir_path.joinpath("puzzle_input.txt")
print(full_path)
array_1 = []
array_2 = []

with open(full_path) as file:
  #num_lines = file.readlines()
  for line in file:
    array.append(line.split())
    #print(line.split())



print(array)


