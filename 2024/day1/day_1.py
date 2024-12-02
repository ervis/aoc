with open("2024/day1/day1.input.txt") as f:
  lines = f.read().splitlines()

left = [int(line.split("   ")[0]) for line in lines]
right = [int(line.split("   ")[1]) for line in lines]
  
s = sum([ abs(a - b) for a, b in zip(sorted(left), sorted(right)) ])
print(s)