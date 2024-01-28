x = [i for i in range(5)]
y = [y for y in range(11)]
z = [z for z in range(8)]
print(x, y, z)

# Returns the numbers without repeating everything
def numbers(x, y, z):
  if x == y == z:
    return x
  elif x == y and x != z:
    return x + z
  elif x != y and y == z:
    return y + z
  else:
    return x + y + z

result = numbers([0, 4, 11], [0, 4, 11], [9,  11])
print(result)
