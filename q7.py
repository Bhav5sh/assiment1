def gcd(x, y):
  """
  Finds the greatest common divisor of x and y.

  Args:
    x: The first number.
    y: The second number.

  Returns:
    The greatest common divisor of x and y.
  """

  if x == 0:
    return y
  else:
    return gcd(y % x, x)


def find_gcd_of_list(list_of_numbers):
  """
  Finds the greatest common divisor of the numbers in the list.

  Args:
    list_of_numbers: A list of numbers.

  Returns:
    The greatest common divisor of the numbers in the list.
  """

  gcd_of_numbers = list_of_numbers[0]
  for number in list_of_numbers[1:]:
    gcd_of_numbers = gcd(gcd_of_numbers, number)

  return gcd_of_numbers


if __name__ == "__main__":
  list_of_numbers = [2, 4, 6, 8, 10]
  gcd_of_numbers = find_gcd_of_list(list_of_numbers)
  print("The greatest common divisor of the numbers in the list is:", gcd_of_numbers)
