url_input = 'https://adventofcode.com/2024/day/2/input'

with open('2024/day2/day2.input.txt') as f:
  lines = [list(map(int, line.split())) for line in f]

successful = 0
for arr in lines:
  diff = 0
  i = 0
  while i < len(arr) - 1:
    if arr[i] == arr[i+1]:
      break
    if diff * (arr[i+1] - arr[i]) < 0: # not increasing or decreasing
      break
    diff = arr[i+1] - arr[i]
    if 0 < abs(diff) <= 3: # out of range
      i += 1
    else:
      break
  if i == len(arr) - 1: # reached the end without problems
    successful += 1
    
print(successful)