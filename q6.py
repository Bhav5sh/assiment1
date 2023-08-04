def even_filter(list_of_numbers):
  """
  Returns a list of only even values from the given list.

  Args:
    list_of_numbers: A list of numbers.

  Returns:
    A list of only even values.
  """

  even_numbers = []
  for number in list_of_numbers:
    if number % 2 == 0:
      even_numbers.append(number)

  return even_numbers


def odd_filter(list_of_numbers):
  """
  Returns a list of only odd values from the given list.

  Args:
    list_of_numbers: A list of numbers.

  Returns:
    A list of only odd values.
  """

  odd_numbers = []
  for number in list_of_numbers:
    if number % 2 != 0:
      odd_numbers.append(number)

  return odd_numbers


if __name__ == "__main__":
  list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  even_numbers = even_filter(list_of_numbers)
  print("Even numbers:", even_numbers)

  dictionary = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}
  odd_numbers = odd_filter(dictionary)
  print("Odd numbers:", odd_numbers)
