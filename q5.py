def trekking_with_friends(a, b, c):
  """
  Calculates the total length of the trek for three friends Suman, Amit, and Ravi.

  Args:
    a: The distance Amit beats Suman by.
    b: The distance Amit beats Ravi by.
    c: The distance Suman beats Ravi by.

  Returns:
    The total length of the trek.
  """

  total_distance = a + b + c
  return total_distance


if __name__ == "__main__":
  a = 10
  b = 20
  c = 12

  total_distance = trekking_with_friends(a, b, c)
  print("Total length of the Track:", total_distance)