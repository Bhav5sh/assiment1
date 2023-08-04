def check_prime(number):
  """
  Checks whether the number is prime or not.

  Args:
    number: The number to check.

  Returns:
    True if the number is prime, False otherwise.
  """

  if number <= 1:
    return False

  for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
      return False

  return True


def twin_primes():
  """
  Generates the list of twin primes and returns them.

  Returns:
    A list of twin primes.
  """

  twin_primes = []
  for i in range(3, 1000):
    if check_prime(i) and check_prime(i + 2):
      twin_primes.append((i, i + 2))

  return twin_primes


if __name__ == "__main__":
  twin_primes = twin_primes()
  print("The list of twin primes less than 1000 is:", twin_primes)
