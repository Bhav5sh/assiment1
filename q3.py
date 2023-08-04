def get_season(month, day):
  """
  Gets the season of a month and day.

  Args:
    month: The month as an integer.
    day: The day as an integer.

  Returns:
    The season as a string.
  """

  seasons = ["Winter", "Spring", "Summer", "Fall"]
  month_days = calendar.monthrange(year, month)[1]

  if day <= 31 and month in (1, 2, 12):
    return seasons[0]
  elif day <= 59 and month in (3, 4, 5):
    return seasons[1]
  elif day <= 90 and month in (6, 7, 8):
    return seasons[2]
  else:
    return seasons[3]


def is_leap_year(year):
  """
  Checks whether a year is a leap year.

  Args:
    year: The year as an integer.

  Returns:
    True if the year is a leap year, False otherwise.
  """

  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def main():
  """
  The main function.
  """

  year = int(input("Enter the year: "))
  month = int(input("Enter the month: "))
  day = int(input("Enter the day: "))

  season = get_season(month, day)
  print("The season is:", season)

  if is_leap_year(year):
    print("The number of days in the year is:", 366)
  else:
    print("The next leap year is:", year + 4)

